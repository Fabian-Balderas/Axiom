from axiom.services.relationship_type import RelationshipType


class Tracer:
    """
    Performs call graph analysis.
    """

    def __init__(self, knowledge_graph):
        self.knowledge_graph = knowledge_graph

    def trace(self, symbol):
        """
        Return every function directly called by a symbol.
        """

        return self.knowledge_graph.get_relationships(
            source=symbol,
            kind=RelationshipType.CALLS,
        )