from axiom.analysis.function_summary import FunctionSummary


class SemanticAnalyzer:
    """
    Performs higher-level analysis using Axiom's knowledge graph.

    The parser discovers facts.

    The knowledge graph stores facts.

    The semantic analyzer interprets those facts.
    """

    def __init__(self, workspace):
        self.workspace = workspace

    def summarize_function(self, function_name):
        """
        Returns everything Axiom currently knows about a function.
        """

        symbol = self.workspace.symbol_index.get_symbol(function_name)

        if symbol is None:
            return None

        graph = self.workspace.knowledge_graph

        return FunctionSummary(
            symbol=symbol,
            defines=graph.get_relationships(
                function_name,
                "defines",
            ),
            references=graph.get_relationships(
                function_name,
                "references",
            ),
            calls=graph.get_relationships(
                function_name,
                "calls",
            ),
            returns=graph.get_relationships(
                function_name,
                "returns",
            ),
        )