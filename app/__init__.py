"""
This module defines the main application class.
"""

import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand

class App:
    """
    The main application class responsible for loading plugins and executing commands.
    """

    class ExitApplication(Exception):
        """Custom exception for exiting the application."""
        pass

    def __init__(self):
        """
        Constructor for the App class.
        """
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """
        Dynamically load all plugins in the plugins directory.
        """
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item != Command:
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        """
        Start the application by loading plugins and registering commands.
        """
        self.load_plugins()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        print("Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip().split()
            print(f"Received command: {user_input}")
            command = user_input[0]
            args = user_input[1:]
            self.command_handler.execute_command(command, args)
