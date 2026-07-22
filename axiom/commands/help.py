from axiom.core.command import Command
from axiom.core.registry import COMMANDS


class HelpCommand(Command):

    name = "help"
    description = "Display all available commands."
    usage = "help"

    def run(self, context, args):
        print("\nAvailable Commands")
        print("------------------")

        for command in COMMANDS.values():
            print(f"{command.name:<12} {command.description}")

        print(f"{'exit':<12} Exit Axiom.")