from dataclasses import dataclass
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