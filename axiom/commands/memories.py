from axiom.core.command import Command


class MemoriesCommand(Command):

    name = "memories"
    description = "Display all stored memories."
    usage = "memories"

    def run(self, context, args):

        memories = context.memory.list()

        if not memories:
            print("No memories stored.")
            return

        print("\nStored Memories")
        print("----------------")

        for key, value in memories.items():
            print(f"{key}: {value}")