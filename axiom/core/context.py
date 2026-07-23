from pathlib import Path

from axiom.config.settings import VERSION
from axiom.services.memory_service import MemoryService
from axiom.services.project_service import ProjectService
from axiom.services.workspace_indexer import WorkspaceIndexer
class Context:
    """
    Shared application state for Axiom.
    Every subsystem lives here.
    """

    def __init__(self):

        self.version = VERSION
        self.workspace = WorkspaceIndexer()
        self.workspace.build_index(Path("."))

        self.memory = MemoryService()
        self.projects = ProjectService()

        self.knowledge = None
        self.reasoning = None
        self.plugins = []

        self.current_project = None