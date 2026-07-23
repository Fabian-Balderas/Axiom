from axiom.skills.manager import SkillManager
from axiom.skills.registry import discover_skills


class Application:
    """
    The central Axiom application.

    Responsible for initializing and coordinating all major systems.
    """

    def __init__(self):
        self.skill_manager = SkillManager()

    def initialize(self):
        """
        Initialize every subsystem.
        """

        for skill in discover_skills():
            self.skill_manager.register(skill)

    def start(self):
        """
        Start the application.
        """

        self.initialize()

        print("Axiom initialized successfully.")
        print(f"Loaded {len(self.skill_manager.list_skills())} skill(s).")