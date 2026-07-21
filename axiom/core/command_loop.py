from axiom.core.command_registry import COMMANDS


def command_loop(context):

    while True:

        user_input = input("\nAxiom > ").strip()

        if user_input == "":
            continue

        parts = user_input.split()

        command = parts[0].lower()
        args = parts[1:]

        if command == "exit":
            print("Shutting down Axiom...")
            break

        handler = COMMANDS[command]

        if callable(handler):
            handler(context, args)
        else:
            handler.run(context, args)