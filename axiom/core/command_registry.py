# Import commands so they register themselves.
from axiom.commands.find import FindCommand
from axiom.commands.status import StatusCommand
from axiom.commands.version import VersionCommand
from axiom.commands.help import HelpCommand
from axiom.commands.remember import RememberCommand
from axiom.core.registry import register, COMMANDS
from axiom.commands.recall import RecallCommand
from axiom.commands.forget import ForgetCommand
from axiom.commands.memories import MemoriesCommand
from axiom.commands.project import ProjectCommand


register(HelpCommand())
register(VersionCommand())
register(StatusCommand())
register(RememberCommand())
register(RecallCommand())
register(ForgetCommand())
register(MemoriesCommand())
register(ProjectCommand())
register(FindCommand())