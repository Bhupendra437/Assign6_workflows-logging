from app.plugins.menu import MenuCommand
from unittest.mock import MagicMock

def test_menu_command(capsys):
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
