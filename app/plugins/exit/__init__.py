import sys
from app.commands import Command


class ExitCommand(Command):
    def execute(self, args):
       raise SystemExit("Exiting...") 
