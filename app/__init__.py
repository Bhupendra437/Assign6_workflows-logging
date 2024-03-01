import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand

from decimal import Decimal, InvalidOperation
class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item != Command:  # Check if it's a subclass of Command and not Command itself
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        # Register commands here
        self.load_plugins()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))  # Register the MenuCommand
        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip().split()  # Split user input into command and arguments
            command = user_input[0]  # First element is the command
            args = user_input[1:]  # Rest of the elements are arguments
            self.command_handler.execute_command(command, args)  # Pass command and arguments to execute_command

