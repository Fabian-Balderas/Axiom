from axiom.analysis.trace_node import TraceNode
from axiom.services.relationship_type import RelationshipType


class Tracer:
    """
    Performs call graph analysis.
    """

    def __init__(self, knowledge_graph):
        self.knowledge_graph = knowledge_graph

    def trace(self, symbol):
        """
        Build a trace tree starting at a symbol.
        """

        return self._trace(symbol, set())

    def _trace(self, symbol, visited):

        node = TraceNode(symbol)

        if symbol in visited:
            return node

        visited.add(symbol)

        relationships = self.knowledge_graph.get_relationships(
            source=symbol,
            kind=RelationshipType.CALLS,
        )

        for relationship in relationships:

            child = self._trace(
                relationship.target,
                visited.copy(),
            )

            node.add_child(child)

        return node