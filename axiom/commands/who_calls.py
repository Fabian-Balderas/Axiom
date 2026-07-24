from axiom.core.command import Command

from axiom.analysis.who_calls import WhoCalls


class WhoCallsCommand(Command):
    """
    Display every function that calls a symbol.
    """

    name = "who-calls"
    description = "Display callers of a symbol."
    usage = "who-calls <symbol>"

    def run(self, context, args):

        if not args:
            print("Usage: who-calls <symbol>")
            return

        symbol = " ".join(args)

        analyzer = WhoCalls(
            context.workspace.knowledge_graph
        )

        relationships = analyzer.find(symbol)

        if not relationships:
            print(f"No callers found for '{symbol}'.")
            return

        print()
        print(symbol)
        print("-" * len(symbol))
        print()
        print("Called By")

        for relationship in sorted(
            relationships,
            key=lambda r: r.source.lower(),
        ):
            print(f"  ├── {relationship.source}")

        print()