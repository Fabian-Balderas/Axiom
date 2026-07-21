def run(context, args):

    if len(args) < 1:
        print("Usage: recall <key>")
        return

    key = args[0]

    value = context.memory.recall(key)

    if value is None:
        print(f'No memory found for "{key}"')
    else:
        print(f'{key} = {value}')