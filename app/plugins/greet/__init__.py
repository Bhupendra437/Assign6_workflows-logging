from app.commands import Command


class GreetCommand(Command):
    def execute(self, args):
        if len(args) != 1:
            print("Usage: greet <name>")
            return

        name = args[0]
        print(f"Hello, {name}!")
