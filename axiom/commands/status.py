from axiom.core.command import Command


class StatusCommand(Command):

    name = "status"
    description = "Display Axiom status."
    usage = "status"

    def run(self, context, args):
        print("\nAxiom Status")
        print("------------")
        print(f"Version : {context.version}")
        print(f"Plugins : {len(context.plugins)}")