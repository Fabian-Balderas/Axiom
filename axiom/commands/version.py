from axiom.core.command import Command


class VersionCommand(Command):

    name = "version"
    description = "Display the current Axiom version."
    usage = "version"

    def run(self, context, args):
        print("\nAxiom Version")
        print("-------------")
        print(f"Version: {context.version}")