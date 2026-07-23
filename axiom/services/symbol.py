from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Symbol:
    """
    Represents a symbol discovered in source code.
    """

    name: str
    kind: str
    file: Path
    line: int

    docstring: str = ""

    methods: list[str] = field(default_factory=list)

    parameters: list[str] = field(default_factory=list)