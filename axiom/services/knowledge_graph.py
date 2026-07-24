from collections import defaultdict

from axiom.services.relationship import Relationship
from axiom.services.relationship_type import RelationshipType


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
        kind: RelationshipType,
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
        source: str | None = None,
        kind: RelationshipType | None = None,
        target: str | None = None,
    ) -> list[Relationship]:
        """
        Return relationships matching the supplied filters.

        Any filter may be omitted.
        """

        relationships: list[Relationship] = []

        if source is not None:
            relationships.extend(self.graph.get(source, []))
        else:
            for rels in self.graph.values():
                relationships.extend(rels)

        if kind is not None:
            relationships = [
                rel
                for rel in relationships
                if rel.kind == kind
            ]

        if target is not None:
            relationships = [
                rel
                for rel in relationships
                if rel.target == target
            ]

        return relationships