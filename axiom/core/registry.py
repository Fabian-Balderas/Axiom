COMMANDS = {}


def register(command):
    """
    Register a command with Axiom.
    """

    COMMANDS[command.name] = command