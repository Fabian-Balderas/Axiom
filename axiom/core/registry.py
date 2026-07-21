COMMANDS = {}


def register(name, handler):
    """
    Register a command with Axiom.
    """
    COMMANDS[name] = handler