from axiom.skills.base import Skill


class HelloSkill(Skill):

    @property
    def name(self):
        return "Hello"

    @property
    def description(self):
        return "Simple test skill."

    def execute(self):
        print("Hello from Axiom!")