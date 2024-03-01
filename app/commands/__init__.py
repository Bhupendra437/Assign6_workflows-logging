# app/commands/__init__.py

"""Module containing command-related classes."""

from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self):
        """Execute the command."""
        # No need for a pass statement here

class CommandHandler:
    """Class to handle commands."""

    def __init__(self):
        """Initialize CommandHandler."""
        self.commands = {}

    def register_command(self, command_name, command: Command):
        """Register a command."""
        self.commands[command_name] = command

    def execute_command(self, command, args):
        """Execute a command."""
        try:
            self.commands[command].execute(args)
        except KeyError:
            print(f"No such command: {command}")
