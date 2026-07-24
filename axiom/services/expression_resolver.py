import ast


class ExpressionResolver:
    """
    Converts Python AST expressions into semantic names that can
    be stored in the knowledge graph.
    """

    def resolve(self, node):

        if node is None:
            return None

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
                return ".".join(reversed(parts))

            return None

        if isinstance(node, ast.Call):
            return self.resolve(node.func)

        if isinstance(node, ast.Constant):
            return repr(node.value)

        return None