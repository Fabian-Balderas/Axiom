from axiom.core.command import Command


class RememberCommand(Command):

    name = "remember"
    description = "Store a key/value pair in memory."
    usage = "remember <key> <value>"

    def run(self, context, args):

        if len(args) < 2:
            print(f"Usage: {self.usage}")
            return

        key = args[0]
        value = " ".join(args[1:])

        context.memory.remember(key, value)

        print(f'Stored "{key}" = "{value}"')