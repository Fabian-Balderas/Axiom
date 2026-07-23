from axiom.core.application import Application
from axiom.core.banner import show_banner
from axiom.core.command_loop import command_loop
from axiom.core.context import Context


class Engine:
    """
    Responsible for starting and running the Axiom application.
    """

    def __init__(self):
        self.application = Application()
        self.context = Context()

    def start(self):
        # Initialize the application and all of its subsystems
        self.application.start()

        # Display the startup banner
        show_banner()

        # Enter the interactive command loop
        command_loop(self.context)