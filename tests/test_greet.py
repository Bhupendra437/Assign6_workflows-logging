"""
Unit tests for the GreetCommand class.
"""

import pytest
from app.plugins.greet import GreetCommand

def test_greet_command(capsys):
    """
    Test the execute method of GreetCommand.
    It should print the correct greeting message.
    """
    # Instantiate GreetCommand
    greet_command = GreetCommand()
    # Execute the command
    greet_command.execute(["World"])
    # Check if the correct greeting message is printed
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
