import pytest
from unittest.mock import patch, MagicMock
from app import App
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

def test_load_plugins():
    # Mocking the CommandHandler class
    with patch('app.CommandHandler') as mock_command_handler:
        # Mocking the plugin module
        with patch('app.importlib.import_module') as mock_import_module:
            # Mocking the plugin name, is_pkg, and item
            mock_import_module.return_value.__iter__.return_value = [('', 'plugin_name', True)]
            mock_item = MagicMock(spec=Command)
            mock_import_module.return_value.plugin_name = mock_item

            # Instantiate the App class
            app = App()

            # Call the load_plugins method
            app.load_plugins()

            # Assert that CommandHandler is instantiated correctly
            mock_command_handler_instance = mock_command_handler.return_value

            # Debugging: print the called attribute of load_plugins method
            print(mock_command_handler_instance.load_plugins.called)

            # Debugging: print the call count of load_plugins method
            print(mock_command_handler_instance.load_plugins.call_count)

            # Debugging: print the arguments passed to load_plugins method
            print(mock_command_handler_instance.load_plugins.call_args)

            # Assert that the load_plugins method is called
            assert mock_command_handler_instance.load_plugins.called

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
            mock_command_handler_instance = mock_command_handler.return_value
            mock_command_handler_instance.load_plugins.assert_called_once()

            # Assert that register_command is called with "menu" and MenuCommand instance
            mock_menu_command_instance = mock_menu_command.return_value
            mock_command_handler_instance.register_command.assert_called_once_with("menu", mock_menu_command_instance)
