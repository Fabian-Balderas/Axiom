from axiom.core.command import Command

from axiom.analysis.tracer import Tracer


class TraceCommand(Command):
    """
    Display every function call made by a symbol.
    """

    name = "trace"
    description = "Trace function calls made by a symbol."
    usage = "trace <symbol>"

    def run(self, context, args):

        if not args:
            print("Usage: trace <symbol>")
            return

        name = " ".join(args)

        tracer = Tracer(
            context.workspace.knowledge_graph
        )

        relationships = tracer.trace(name)

        if not relationships:
            print(f"No calls found for '{name}'.")
            return

        print()
        print(name)
        print("-" * len(name))
        print()
        print("Calls")

        for relationship in sorted(
            relationships,
            key=lambda r: r.target.lower(),
        ):
            print(f"  ├── {relationship.target}")

        print()