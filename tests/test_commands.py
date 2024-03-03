"""Tests for the Command and CommandHandler classes in app.commands."""

from unittest.mock import MagicMock, patch
import pytest
from app.commands import Command, CommandHandler

class MockCommand(Command):
    """Mock subclass of Command for testing purposes."""
    def execute(self):
        """Mock execute method."""
        print("Executing MockCommand")

def test_register_command():
    """Test that commands can be registered correctly."""
    command_handler = CommandHandler()
    mock_command = MockCommand()

    command_handler.register_command("mock", mock_command)
    assert "mock" in command_handler.commands
    assert command_handler.commands["mock"] == mock_command

def test_execute_command():
    """Test that registered commands can be executed."""
    command_handler = CommandHandler()
    mock_command = MockCommand()

    with patch.object(MockCommand, 'execute') as mock_execute:
        command_handler.register_command("mock", mock_command)
        command_handler.execute_command("mock", [])
        mock_execute.assert_called_once()

def test_execute_nonexistent_command(capsys):
    """Test that executing a nonexistent command prints an error message."""
    command_handler = CommandHandler()
    command_handler.execute_command("nonexistent", [])

    captured = capsys.readouterr()
    assert "No such command: nonexistent" in captured.out
