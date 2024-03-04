"""
This module contains unit tests for the MenuCommand class.
"""

from unittest.mock import MagicMock
import pytest
from app.plugins.menu import MenuCommand
from app.commands import CommandHandler

@pytest.fixture
def command_handler():
    """
    Fixture for creating a mock CommandHandler.
    """
    handler = CommandHandler()
    handler.commands = {
        'command1': MagicMock(),
        'command2': MagicMock(),
        'command3': MagicMock()
    }
    return handler

@pytest.fixture
def menu_command(command_handler):
    """
    Fixture for creating an instance of MenuCommand.
    """
    return MenuCommand(command_handler)

def test_menu_command_execution(menu_command, capsys):
    """
    Test the execution of the menu command.
    """
    menu_command.execute([])
    captured = capsys.readouterr()
    expected_output = "Available commands:\n- command1\n- command2\n- command3\n"
    assert captured.out == expected_output
