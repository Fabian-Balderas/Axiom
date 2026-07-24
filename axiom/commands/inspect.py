from axiom.core.command import Command

from axiom.services.relationship_type import RelationshipType


class InspectCommand(Command):
    """
    Display detailed information about a symbol.
    """

    name = "inspect"
    description = "Inspect a symbol."
    usage = "inspect <symbol>"

    def run(self, context, args):

        if not args:
            print("Usage: inspect <symbol>")
            return

        name = " ".join(args)

        symbol = context.workspace.symbol_index.get_symbol(name)

        if symbol is None:
            print(f"No symbol named '{name}' was found.")
            return

        print()
        print(f"Name : {symbol.name}")
        print(f"Kind : {symbol.kind.capitalize()}")
        print(f"File : {symbol.file}")
        print(f"Line : {symbol.line}")

        if symbol.docstring:
            print()
            print("Documentation")
            print("-------------")
            print(symbol.docstring)

        if symbol.methods:
            print()
            print("Methods")
            print("-------")

            for method in symbol.methods:
                print(method)

        if symbol.parameters:
            print()
            print("Parameters")
            print("----------")

            for parameter in symbol.parameters:
                print(parameter)

        relationships = context.workspace.knowledge_graph

        sections = [
            ("Defines", RelationshipType.DEFINES),
            ("References", RelationshipType.REFERENCES),
            ("Calls", RelationshipType.CALLS),
            ("Contains", RelationshipType.CONTAINS),
            ("Imports", RelationshipType.IMPORTS),
            ("Inherits", RelationshipType.INHERITS),
        ]

        printed_header = False

        for title, kind in sections:

            rels = relationships.get_relationships(
                source=symbol.name,
                kind=kind,
            )

            if not rels:
                continue

            if not printed_header:
                print()
                print("Relationships")
                print("-------------")
                printed_header = True

            print()
            print(title)
            print("-" * len(title))

            for rel in rels:
                print(rel.target)

        print()