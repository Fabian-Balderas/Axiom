def run(context, args):

    if len(args) < 1:
        print("Usage: forget <key>")
        return

    key = args[0]

    if context.memory.forget(key):
        print(f'Forgot "{key}"')
    else:
        print(f'No memory found for "{key}"')