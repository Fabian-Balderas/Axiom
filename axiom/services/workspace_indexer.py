from dataclasses import dataclass, field
from pathlib import Path
import os
import ast

from axiom.services.knowledge_graph import KnowledgeGraph
from axiom.services.symbol import Symbol
from axiom.services.symbol_index import SymbolIndex


@dataclass
class FileInfo:
    """
    Represents a single file within the workspace.
    """

    path: Path
    name: str
    extension: str
    size: int

    classes: list[str] = field(default_factory=list)
    functions: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)


class WorkspaceIndexer:
    """
    Indexes files within the current Axiom workspace.
    """

    def __init__(self):
        self.files: list[FileInfo] = []
        self.symbol_index = SymbolIndex()
        self.knowledge_graph = KnowledgeGraph()

    def build_index(self, root: Path):
        """
        Scan the workspace and collect information about every file.
        """

        self.files.clear()
        self.symbol_index.clear()
        self.knowledge_graph.clear()

        ignored_dirs = {
            "__pycache__",
            ".git",
            ".venv",
            "venv",
            ".idea",
            ".vscode",
        }

        for current_path, dirnames, filenames in os.walk(root):

            # Prevent os.walk() from descending into ignored directories.
            dirnames[:] = [
                d
                for d in dirnames
                if d not in ignored_dirs
            ]

            for filename in filenames:

                full_path = Path(current_path) / filename

                file_info = FileInfo(
                    path=full_path,
                    name=full_path.stem,
                    extension=full_path.suffix,
                    size=full_path.stat().st_size,
                )

                if full_path.suffix == ".py":
                    self.parse_python_file(file_info)

                self.files.append(file_info)

    def find_file(self, name: str) -> list[FileInfo]:
        """
        Find files by name (case-insensitive).
        """

        name = name.lower()

        return [
            file
            for file in self.files
            if name in file.name.lower()
        ]

    def parse_python_file(self, file_info: FileInfo):
        """
        Extract classes, functions, imports, and docstrings
        from a Python source file.
        """

        try:
            source = file_info.path.read_text(encoding="utf-8")
            tree = ast.parse(source)

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):

                    docstring = ast.get_docstring(node) or ""

                    methods = [
                        child.name
                        for child in node.body
                        if isinstance(child, ast.FunctionDef)
                    ]

                    # Build Knowledge Graph relationships
                    for method in methods:
                        self.knowledge_graph.add_relationship(
                            source=node.name,
                            kind="contains",
                            target=method,
                        )

                    symbol = Symbol(
                        name=node.name,
                        kind="class",
                        file=file_info.path,
                        line=node.lineno,
                        docstring=docstring,
                        methods=methods,
                    )

                    self.symbol_index.add(symbol)
                    file_info.classes.append(node.name)

                elif isinstance(node, ast.FunctionDef):

                    docstring = ast.get_docstring(node) or ""

                    parameters = [
                        arg.arg
                        for arg in node.args.args
                    ]

                    symbol = Symbol(
                        name=node.name,
                        kind="function",
                        file=file_info.path,
                        line=node.lineno,
                        docstring=docstring,
                        parameters=parameters,
                    )

                    self.symbol_index.add(symbol)
                    file_info.functions.append(node.name)

                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        file_info.imports.append(alias.name)

                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""

                    for alias in node.names:
                        if module:
                            file_info.imports.append(f"{module}.{alias.name}")
                        else:
                            file_info.imports.append(alias.name)

        except Exception:
            # Skip files that cannot be parsed.
            pass