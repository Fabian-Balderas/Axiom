from dataclasses import dataclass


@dataclass
class Symbol:
    """
    Represents a named symbol discovered in source code.
    """

    name: str
    kind: str
    line: int