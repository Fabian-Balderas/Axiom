from abc import ABC, abstractmethod


class Skill(ABC):
    """
    Base class for every Axiom skill.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name of the skill."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Brief description of what the skill does."""
        pass

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def author(self) -> str:
        return "Axiom"

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Run the skill."""
        pass

    def stop(self):
        """Optional cleanup."""
        pass

    def help(self) -> str:
        return self.description