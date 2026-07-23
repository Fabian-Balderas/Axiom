from dataclasses import dataclass


@dataclass
class Relationship:
    """
    Represents a relationship between two symbols.
    """

    source: str
    kind: str
    target: str