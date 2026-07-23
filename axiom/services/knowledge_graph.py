from collections import defaultdict

from axiom.services.relationship import Relationship


class KnowledgeGraph:
    """
    Stores relationships between symbols.
    """

    def __init__(self):
        self.graph: dict[str, list[Relationship]] = defaultdict(list)

    def clear(self):
        self.graph.clear()

    def add_relationship(
        self,
        source: str,
        kind: str,
        target: str,
    ):
        """
        Add a relationship between two symbols.
        """

        self.graph[source].append(
            Relationship(
                source=source,
                kind=kind,
                target=target,
            )
        )

    def get_relationships(
        self,
        source: str,
    ) -> list[Relationship]:
        """
        Return every relationship originating from a symbol.
        """

        return self.graph.get(source, [])