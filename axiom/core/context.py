from axiom.config.settings import VERSION
from axiom.services.memory_service import MemoryService
from axiom.services.project_service import ProjectService

class Context:
    """
    Shared application state for Axiom.
    Every subsystem lives here.
    """

    def __init__(self):

        self.version = VERSION

        self.memory = MemoryService()
        self.projects = ProjectService()

        self.knowledge = None
        self.reasoning = None
        self.plugins = []

        self.current_project = None