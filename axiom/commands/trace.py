from axiom.core.command import Command

from axiom.analysis.tracer import Tracer
from axiom.rendering.tree_renderer import TreeRenderer


class TraceCommand(Command):
    """
    Display the complete call tree for a symbol.
    """

    name = "trace"
    description = "Trace function calls made by a symbol."
    usage = "trace <symbol>"

    def run(self, context, args):

        if not args:
            print("Usage: trace <symbol>")
            return

        symbol = " ".join(args)

        tracer = Tracer(
            context.workspace.knowledge_graph
        )

        tree = tracer.trace(symbol)

        print()

        renderer = TreeRenderer()
        renderer.render(tree)

        print()