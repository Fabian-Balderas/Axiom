def run(context, args):

    if len(args) < 2:
        print("Usage: remember <key> <value>")
        return

    key = args[0]
    value = " ".join(args[1:])

    context.memory.remember(key, value)

    print(f'Stored "{key}" = "{value}"')