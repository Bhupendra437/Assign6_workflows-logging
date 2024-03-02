"""
Test cases for the App class.
"""

from unittest.mock import patch, MagicMock
import pytest
from app import App
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

def test_load_plugins():
    """
    Test loading plugins.
    """
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

            # Assert that the load_plugins method is called
            mock_command_handler_instance.load_plugins.assert_called_once()

def test_start():
    """
    Test starting the application.
    """
    # Mocking the CommandHandler class
    with patch('app.CommandHandler'), \
            patch('app.plugins.menu.MenuCommand'):
        # Instantiate the App class
        app = App()

        # Defining a predefined input
        predefined_input = ['exit']

        # Define a generator function to yield predefined input indefinitely
        def input_side_effect(prompt):
            while predefined_input:
                yield predefined_input.pop(0)

        # Patching the input function with the generator
        with patch('builtins.input', side_effect=input_side_effect):
            # Calling the start method
            with pytest.raises(App.ExitApplication):
                app.start()
