from typing import Dict

from axiom.skills.base import Skill


class SkillManager:
    """
    Registers and manages all available Axiom skills.
    """

    def __init__(self):
        self._skills: Dict[str, Skill] = {}

    def register(self, skill: Skill):
        """Register a new skill."""
        self._skills[skill.name.lower()] = skill

    def get(self, name: str) -> Skill | None:
        """Retrieve a skill by name."""
        return self._skills.get(name.lower())

    def list_skills(self) -> list[str]:
        """Return the names of all registered skills."""
        return sorted(skill.name for skill in self._skills.values())

    def execute(self, name: str, *args, **kwargs):
        """Execute a registered skill."""
        skill = self.get(name)

        if skill is None:
            raise ValueError(f"Unknown skill: {name}")

        return skill.execute(*args, **kwargs)