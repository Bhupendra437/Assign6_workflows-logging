"""
Unit tests for the commands module.
"""

from unittest.mock import patch, MagicMock
import pytest
from app import App
from app.commands import CommandHandler
from app.plugins.menu import MenuCommand

def test_load_plugins_registers_plugin_command():
    """
    Test that the load_plugins method registers plugin commands correctly.
    """
    with patch('app.pkgutil.iter_modules'):
        with patch('app.importlib.import_module') as mock_import_module:
            mock_plugin_module = MagicMock()
            mock_plugin_module.__iter__.return_value = [('plugin_name', MagicMock(), True)]
            mock_import_module.return_value = mock_plugin_module

            with patch('app.commands.CommandHandler') as mock_command_handler:
                app = App()
                app.load_plugins()
                mock_command_handler_instance = mock_command_handler.return_value
                mock_command_handler_instance.register_command.assert_called_once_with('plugin_name', MagicMock())

def test_start_registers_menu_command_and_starts():
    """
    Test that the start method registers the menu command and starts the application correctly.
    """
    with patch('app.commands.CommandHandler') as mock_command_handler:
        with patch('app.plugins.menu.MenuCommand') as mock_menu_command:
            app = App()
            predefined_input = ['exit']

            with patch('builtins.input', side_effect=predefined_input):
                with pytest.raises(App.ExitApplication):
                    app.start()

            mock_command_handler_instance = mock_command_handler.return_value
            mock_command_handler_instance.load_plugins.assert_called_once()

            mock_menu_command_instance = mock_menu_command.return_value
            mock_command_handler_instance.register_command.assert_called_once_with("menu", mock_menu_command_instance)
