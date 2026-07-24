from axiom.services.relationship_type import RelationshipType


class WhoCalls:
    """
    Finds every symbol that calls another symbol.
    """

    def __init__(self, knowledge_graph):
        self.knowledge_graph = knowledge_graph

    def find(self, symbol):
        return self.knowledge_graph.get_relationships(
            target=symbol,
            kind=RelationshipType.CALLS,
        )