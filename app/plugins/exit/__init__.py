import sys
from app.commands import Command


class ExitCommand(Command):
    name = 'exit'
    def execute(self, args):
       raise SystemExit("Exiting...") 
