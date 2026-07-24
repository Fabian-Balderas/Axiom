import ast

from axiom.services.relationship_type import RelationshipType
from axiom.services.symbol import Symbol


class PythonAstVisitor(ast.NodeVisitor):
    """
    Visits Python AST nodes and builds Axiom's knowledge model.
    """

    def __init__(self, workspace, file_info):
        self.workspace = workspace
        self.file_info = file_info
        self.current_class = None
        self.current_function = None

    def get_qualified_name(self, node):
        """
        Returns the fully qualified name represented by an AST node.

        Examples:
            print
            ast.parse
            visitor.visit
            file_info.path.read_text
        """

        if isinstance(node, ast.Name):
            return node.id

        if isinstance(node, ast.Attribute):

            parts = []

            current = node

            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value

            if isinstance(current, ast.Name):
                parts.append(current.id)
            else:
                return None

            return ".".join(reversed(parts))

        return None

    def visit_ClassDef(self, node):

        self.current_class = node.name

        docstring = ast.get_docstring(node) or ""

        methods = [
            child.name
            for child in node.body
            if isinstance(child, ast.FunctionDef)
        ]

        # Contains relationships
        for method in methods:
            self.workspace.knowledge_graph.add_relationship(
                source=node.name,
                kind=RelationshipType.CONTAINS,
                target=method,
            )

        # Inheritance relationships
        for base in node.bases:

            target = self.get_qualified_name(base)

            if target is None:
                continue

            self.workspace.knowledge_graph.add_relationship(
                source=node.name,
                kind=RelationshipType.INHERITS,
                target=target,
            )

        symbol = Symbol(
            name=node.name,
            kind="class",
            file=self.file_info.path,
            line=node.lineno,
            docstring=docstring,
            methods=methods,
        )

        self.workspace.symbol_index.add(symbol)
        self.file_info.classes.append(node.name)

        self.generic_visit(node)

        self.current_class = None

    def visit_FunctionDef(self, node):

        self.current_function = node.name

        docstring = ast.get_docstring(node) or ""

        parameters = [
            arg.arg
            for arg in node.args.args
        ]

        symbol = Symbol(
            name=node.name,
            kind="function",
            file=self.file_info.path,
            line=node.lineno,
            docstring=docstring,
            parameters=parameters,
        )

        self.workspace.symbol_index.add(symbol)
        self.file_info.functions.append(node.name)

        self.generic_visit(node)

        self.current_function = None

    def visit_Import(self, node):

        for alias in node.names:

            self.workspace.knowledge_graph.add_relationship(
                source=self.file_info.path.stem,
                kind=RelationshipType.IMPORTS,
                target=alias.name,
            )

        self.generic_visit(node)

    def visit_ImportFrom(self, node):

        module = node.module or ""

        for alias in node.names:

            if module:
                target = f"{module}.{alias.name}"
            else:
                target = alias.name

            self.workspace.knowledge_graph.add_relationship(
                source=self.file_info.path.stem,
                kind=RelationshipType.IMPORTS,
                target=target,
            )

        self.generic_visit(node)

    def visit_Call(self, node):

        # Ignore calls that aren't inside a function.
        if self.current_function is None:
            self.generic_visit(node)
            return

        target = self.get_qualified_name(node.func)

        if target:
            self.workspace.knowledge_graph.add_relationship(
                source=self.current_function,
                kind=RelationshipType.CALLS,
                target=target,
            )

        self.generic_visit(node)

    def visit_Name(self, node):
        """
        Records symbol references inside functions.
        """

        # Ignore names outside functions.
        if self.current_function is None:
            self.generic_visit(node)
            return

        self.workspace.knowledge_graph.add_relationship(
            source=self.current_function,
            kind=RelationshipType.REFERENCES,
            target=node.id,
        )

        self.generic_visit(node)

    def visit_Assign(self, node):
        """
        Records variables defined by assignment.
        """

        # Ignore assignments outside functions.
        if self.current_function is None:
            self.generic_visit(node)
            return

        for target in node.targets:

            if isinstance(target, ast.Name):

                self.workspace.knowledge_graph.add_relationship(
                    source=self.current_function,
                    kind=RelationshipType.DEFINES,
                    target=target.id,
                )

        self.generic_visit(node)