from axiom.core.command import Command

from axiom.analysis.semantic_analyzer import SemanticAnalyzer


class ExplainCommand(Command):
    """
    Explain what a function does using Axiom's semantic analysis.
    """

    name = "explain"
    description = "Explain a function."
    usage = "explain <function>"

    def run(self, context, args):

        if not args:
            print("Usage: explain <function>")
            return

        name = " ".join(args)

        analyzer = SemanticAnalyzer(context.workspace)
        summary = analyzer.summarize_function(name)

        if summary is None:
            print(f"No function named '{name}' was found.")
            return

        symbol = summary.symbol

        print()
        print(f"Function : {symbol.name}")
        print(f"File     : {symbol.file}")
        print(f"Line     : {symbol.line}")

        if symbol.docstring:
            print()
            print("Documentation")
            print("-------------")
            print(symbol.docstring)

        if summary.defines:
            print()
            print("Creates")
            print("-------")

            for relationship in summary.defines:
                print(f"• {relationship.target}")

        if summary.references:
            print()
            print("Depends On")
            print("----------")

            for relationship in summary.references:
                print(f"• {relationship.target}")

        if summary.calls:
            print()
            print("Calls")
            print("-----")

            for relationship in summary.calls:
                print(f"• {relationship.target}")

        if summary.returns:
            print()
            print("Returns")
            print("-------")

            for relationship in summary.returns:
                print(f"• {relationship.target}")

        print()