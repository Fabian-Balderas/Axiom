from enum import Enum


class RelationshipType(str, Enum):
    """
    The different kinds of relationships Axiom understands.
    """

    CONTAINS = "contains"
    IMPORTS = "imports"
    INHERITS = "inherits"
    CALLS = "calls"
    REFERENCES = "references"

    DEFINES = "defines"
    RETURNS = "returns"