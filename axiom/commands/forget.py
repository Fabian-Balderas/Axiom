from axiom.core.command import Command


class ForgetCommand(Command):

    name = "forget"
    description = "Remove a value from memory."
    usage = "forget <key>"

    def run(self, context, args):

        if len(args) < 1:
            print(f"Usage: {self.usage}")
            return

        key = args[0]

        if context.memory.forget(key):
            print(f'Forgot "{key}"')
        else:
            print(f'No memory found for "{key}"')