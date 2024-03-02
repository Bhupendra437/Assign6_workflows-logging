"""
This module defines the GreetCommand class, which is a command to greet a person.
"""
from app.commands import Command

class GreetCommand(Command):
    # pylint: disable=arguments-differ
    """
    A command to greet a person.
    """
    def execute(self, args):
        """
        Execute the greet command.

        Args:
            args (list): A list containing the name of the person to greet.
        """
        if len(args) != 1:
            print("Usage: greet <name>")
            return

        name = args[0]
        print(f"Hello, {name}!")
