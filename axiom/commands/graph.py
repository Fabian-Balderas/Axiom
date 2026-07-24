from axiom.core.command import Command


class GraphCommand(Command):
    """
    Display the relationships for a symbol.
    """

    name = "graph"
    description = "Display relationships for a symbol."
    usage = "graph <symbol>"

    def run(self, context, args):

        if not args:
            print("Usage: graph <symbol>")
            return

        name = " ".join(args)

        relationships = context.workspace.knowledge_graph.get_relationships(name)

        if not relationships:
            print(f"No relationships found for '{name}'.")
            return

        print()
        print(name)
        print("-" * len(name))

        grouped = {}

        for relationship in relationships:
            grouped.setdefault(
                relationship.kind,
                []
            ).append(
                relationship.target
            )

        for kind, targets in grouped.items():

            print()
            print(f"{kind.value.capitalize()}")

            for target in sorted(targets):
                print(f"  ├── {target}")

        print()