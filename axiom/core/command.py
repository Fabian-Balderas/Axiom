class Command:
    """
    Base class for all Axiom commands.
    """

    name = ""
    description = ""
    usage = ""

    def run(self, context, args):
        raise NotImplementedError("Commands must implement run().")