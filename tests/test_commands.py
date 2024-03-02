"""
Unit tests for the commands module.
"""

from unittest.mock import patch, MagicMock
import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand
from app.commands import Command

def test_load_plugins_registers_plugin_command():
    """
    Test that the load_plugins method registers plugin commands correctly.
    """
    with patch('app.pkgutil.iter_modules'):
        with patch('app.importlib.import_module') as mock_import_module:
            mock_plugin_module = MagicMock()
            mock_command_class = MagicMock(spec=Command)
            mock_plugin_module.__iter__.return_value = [('plugin_name', mock_command_class, True)]
            mock_import_module.return_value = mock_plugin_module

            app = App()
            with patch.object(app, 'command_handler') as mock_command_handler:
                app.load_plugins()
                mock_command_handler.register_command.assert_called_once_with('plugin_name', mock_command_class)

def test_start_registers_menu_command_and_starts():
    """
    Test that the start method registers the menu command and starts the application correctly.
    """
    with patch('app.commands.CommandHandler') as mock_command_handler:
        with patch('app.plugins.menu.MenuCommand') as mock_menu_command:
            app = App()
            predefined_input = ['exit']

            with patch('builtins.input', side_effect=predefined_input):
                try:
                    app.start()
                except SystemExit as e:
                    assert str(e) == "Exiting..."
                else:
                    pytest.fail("Expected SystemExit not raised")

    # You can also add additional assertions here to check that
    # the menu command was registered correctly, etc.
