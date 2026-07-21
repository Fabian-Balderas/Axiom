# Import commands so they register themselves.

from axiom.commands import help
from axiom.commands import status
from axiom.commands import remember
from axiom.commands import recall
from axiom.commands import memories
from axiom.commands import forget
from axiom.commands import project

from axiom.commands.version import VersionCommand
from axiom.core.registry import register, COMMANDS

register("version", VersionCommand())