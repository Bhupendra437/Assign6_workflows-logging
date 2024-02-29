from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.greet import GreetCommand
from app.commands.calc import CalcCommand
from app.commands.menu import MenuCommand
from decimal import Decimal, InvalidOperation
class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("calc", CalcCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))  # Register the MenuCommand

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            user_input = input(">>> ").strip().split()  # Split user input into command and arguments
            command = user_input[0]  # First element is the command
            args = user_input[1:]  # Rest of the elements are arguments
            self.command_handler.execute_command(command, args)  # Pass command and arguments to execute_command

