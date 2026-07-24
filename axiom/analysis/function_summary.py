class FunctionSummary:
    """
    Represents Axiom's semantic understanding of a function.
    """

    def __init__(
        self,
        symbol,
        defines,
        references,
        calls,
        returns,
    ):
        self.symbol = symbol
        self.defines = defines
        self.references = references
        self.calls = calls
        self.returns = returns