from axiom.core.command import Command


class RecallCommand(Command):

    name = "recall"
    description = "Retrieve a value from memory."
    usage = "recall <key>"

    def run(self, context, args):

        if len(args) < 1:
            print(f"Usage: {self.usage}")
            return

        key = args[0]

        value = context.memory.recall(key)

        if value is None:
            print(f'No memory found for "{key}"')
        else:
            print(f"{key} = {value}")