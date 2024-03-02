"""
Unit tests for the MenuCommand class.
"""

from unittest.mock import MagicMock
from app.plugins.menu import MenuCommand

def test_menu_command(capsys):
    """
    Test the execute method of MenuCommand.
    It should print the correct menu.
    """
    # Create a mock CommandHandler
    command_handler_mock = MagicMock()
    # Set up the MenuCommand with the mock CommandHandler
    menu_command = MenuCommand(command_handler_mock)
    # Execute the command
    menu_command.execute([])
    # Check if the correct menu is printed
    captured = capsys.readouterr()
    expected_output = "Available commands:\n"
    assert captured.out == expected_output
