from dataclasses import dataclass, field
from pathlib import Path
import os
import ast

from axiom.services.python_ast_visitor import PythonAstVisitor
from axiom.services.knowledge_graph import KnowledgeGraph
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
        Parse a Python file using the PythonAstVisitor.
        """

        try:
            source = file_info.path.read_text(encoding="utf-8")
            tree = ast.parse(source)

            visitor = PythonAstVisitor(self, file_info)
            visitor.visit(tree)

        except Exception:
            # Skip files that cannot be parsed.
            pass