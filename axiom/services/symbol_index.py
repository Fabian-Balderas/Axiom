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

    def find(self, name: str) -> list[Symbol]:
        name = name.lower()

        return [
            symbol
            for symbol in self.symbols
            if name in symbol.name.lower()
        ]