from axiom.core.banner import show_banner
from axiom.core.command_loop import command_loop
from axiom.core.context import Context


class Engine:

    def __init__(self):
        self.context = Context()

    def start(self):
        show_banner()
        command_loop(self.context)