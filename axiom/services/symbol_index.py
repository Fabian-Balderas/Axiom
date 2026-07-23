from .symbol import Symbol


class SymbolIndex:
    """
    Stores every symbol discovered in the workspace.
    """

    def __init__(self):
        self.symbols: list[Symbol] = []

    def add(self, symbol: Symbol):
        self.symbols.append(symbol)

    def clear(self):
        self.symbols.clear()

    def find_symbol(self, query: str) -> list[Symbol]:
        """
        Return all symbols whose names contain the query.
        Search is case-insensitive.
        """

        query = query.lower()

        return [
            symbol
            for symbol in self.symbols
            if query in symbol.name.lower()
        ]

    def get_symbol(self, name: str) -> Symbol | None:
        """
        Return the first symbol whose name exactly matches.
        Search is case-insensitive.
        """

        name = name.lower()

        for symbol in self.symbols:
            if symbol.name.lower() == name:
                return symbol

        return None