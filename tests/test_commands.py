import pytest
from unittest.mock import patch, MagicMock
from app import App
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

def test_load_plugins():
    # Mocking the import_module function in the app module
    with patch('app.importlib.import_module') as mock_import_module:
        # Mocking the plugin module
        mock_plugin_module = MagicMock()
        mock_plugin_module.__iter__.return_value = [('plugin_name', MagicMock(), True)]
        mock_import_module.return_value = mock_plugin_module
        
        # Mocking the CommandHandler class
        with patch('app.CommandHandler') as mock_command_handler:
            # Instantiate the App class
            app = App()

            # Call the load_plugins method
            app.load_plugins()

            # Assert that CommandHandler is instantiated correctly
            mock_command_handler_instance = mock_command_handler.return_value

            # Assert that the register_command method is called with the correct arguments
            mock_command_handler_instance.register_command.assert_called_once_with('plugin_name', MagicMock())

def test_start():
    # Mocking the CommandHandler class
    with patch('app.CommandHandler') as mock_command_handler:
        # Mocking the MenuCommand class
        with patch('app.plugins.menu.MenuCommand') as mock_menu_command:
            # Instantiate the App class
            app = App()

            # Call the start method
            app.start()

            # Assert that load_plugins is called
            assert app.load_plugins.called

            # Assert that register_command is called with "menu" and MenuCommand instance
            mock_command_handler_instance = mock_command_handler.return_value
            mock_menu_command_instance = mock_menu_command.return_value
            mock_command_handler_instance.register_command.assert_called_once_with("menu", mock_menu_command_instance)
