def run(context, args):

    memories = context.memory.list()

    if not memories:
        print("No memories stored.")
        return

    print("\nStored Memories")
    print("----------------")

    for key, value in memories.items():
        print(f"{key}: {value}")