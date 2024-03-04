"""
This module contains unit tests for the GreetCommand class.
"""

from unittest.mock import patch
import pytest
from app.plugins.greet import GreetCommand

@pytest.fixture
def greet_command():
    """
    Fixture for creating an instance of GreetCommand.
    """
    return GreetCommand()

def test_greet_command_with_no_args(greet_command, capsys):
    """
    Test the greet command with no arguments.
    """
    greet_command.execute([])
    captured = capsys.readouterr()
    assert captured.out == "Usage: greet <name>\n"

def test_greet_command_with_one_arg(greet_command, capsys):
    """
    Test the greet command with one argument.
    """
    greet_command.execute(['John'])
    captured = capsys.readouterr()
    assert captured.out == "Hello, John!\n"

def test_greet_command_with_multiple_args(greet_command, capsys):
    """
    Test the greet command with multiple arguments.
    """
    greet_command.execute(['John', 'Doe'])
    captured = capsys.readouterr()
    assert captured.out == "Usage: greet <name>\n"
