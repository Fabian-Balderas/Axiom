from axiom.core.command import Command


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
                print(f"{method}()")

        if symbol.parameters:
            print()
            print("Parameters")
            print("----------")

            for parameter in symbol.parameters:
                print(parameter)

        print()