from axiom.core.command import Command


class FindCommand(Command):
    """
    Search Axiom's symbol index.
    """

    name = "find"
    description = "Search the workspace symbol index."
    usage = "find <symbol>"

    def run(self, context, args):

        if not args:
            print("Usage: find <symbol>")
            return

        query = " ".join(args)

        results = context.workspace.symbol_index.find_symbol(query)

        if not results:
            print(f"No symbols found matching '{query}'.")
            return

        print(f"\nFound {len(results)} symbol(s):\n")

        for symbol in results:
            print(f"{symbol.kind.capitalize():<10} {symbol.name}")
            print(f"  File: {symbol.file}")
            print(f"  Line: {symbol.line}")
            print()