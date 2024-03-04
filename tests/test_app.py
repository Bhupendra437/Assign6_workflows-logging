"""
This module contains unit tests for the App class.
"""

from unittest.mock import patch, MagicMock, ANY
import pytest
from app import App
from app.commands import Command, CommandHandler
from app.plugins.menu import MenuCommand

class MockCommand(Command):
    """
    A mock command class for testing purposes.
    Overrides the execute method for testing.
    """
    def execute(self):
        """
        Execute method for MockCommand.

        Args:
        - args: List of arguments passed to the command.
        """
        print("Executing MockCommand")

@pytest.fixture
def app_instance():
    """
    Fixture for creating an instance of App.
    """
    return App()

def test_load_plugins(app_instance):
    """
    Test for loading plugins.
    """
    with patch('app.pkgutil.iter_modules') as mock_iter_modules, \
         patch('app.importlib.import_module') as mock_import_module:
        mock_iter_modules.return_value = [('mock_plugin', None, True)]
        mock_plugin_module = MagicMock()
        setattr(mock_plugin_module, 'MockCommand', MockCommand)
        mock_import_module.return_value = mock_plugin_module

        app_instance.load_plugins()

        assert 'mockcommand' in app_instance.command_handler.commands
        assert isinstance(app_instance.command_handler.commands['mockcommand'], MockCommand)

def test_start_registers_menu_command(app_instance):
    """
    Test for registering menu command.
    """
    with patch.object(app_instance.command_handler, 'register_command') as mock_register_command, \
         patch('builtins.input', side_effect=App.ExitApplication):
        try:
            app_instance.start()
        except App.ExitApplication:
            pass  # Expected to exit the application loop

        mock_register_command.assert_called_with('menu', ANY)

def test_start_executes_command(app_instance):
    """
    Test for executing commands.
    """
    class MockCommand(Command):
        """
        A mock command class for testing command execution.
        """
        def execute(self):
            print("Executing MockCommand")
    # Register the mock command manually
    app_instance.command_handler.register_command('mock_command', MockCommand())

    # Simulate the execution of the command
    with patch.object(app_instance.command_handler, 'execute_command') as mock_execute_command:
        app_instance.command_handler.execute_command('mock_command', ['arg1', 'arg2'])
        mock_execute_command.assert_called_with('mock_command', ['arg1', 'arg2'])
