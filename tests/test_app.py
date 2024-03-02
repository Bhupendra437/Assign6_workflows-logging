"""
Module containing tests for the App class.
"""

from unittest.mock import patch, MagicMock, call
import pytest
from app import App
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

@pytest.fixture
def app_instance():
    """
    Fixture to create an instance of the App class for testing.
    """
    return App()

def test_load_plugins_success(app_instance):
    """
    Test loading plugins successfully.
    """
    with patch('app.importlib.import_module') as mock_import_module:
        # Mocking the plugin name, is_pkg, and item
        mock_import_module.return_value.__iter__.return_value = [('', 'plugin_name', True)]
        mock_item = MagicMock(spec=Command)
        mock_import_module.return_value.plugin_name = mock_item

        app_instance.load_plugins()

        # Assert that CommandHandler is instantiated correctly
        assert isinstance(app_instance.command_handler, CommandHandler)

def test_load_plugins_exception(app_instance, caplog):
    """
    Test handling exceptions during plugin loading.
    """
    with patch('app.importlib.import_module') as mock_import_module:
        mock_import_module.side_effect = Exception("Mocked exception")
        app_instance.load_plugins()
        assert "Error loading plugins" in caplog.text

def test_start_exit_application(app_instance, capsys):
    """
    Test starting the application and exiting.
    """
    predefined_input = ['exit']
    input_index = [0]  # Use a list to make it mutable

    def input_side_effect(prompt):
        if input_index[0] < len(predefined_input):
            result = predefined_input[input_index[0]]
            input_index[0] += 1
            return result
        return ''

    with patch('builtins.input', side_effect=input_side_effect):
        with pytest.raises(SystemExit):  # Expecting SystemExit instead of App.ExitApplication
            app_instance.start()

    captured = capsys.readouterr()
    assert "Type 'exit' to exit." in captured.out

def test_start_execute_command(app_instance, capsys):
    """
    Test starting the application and executing a command.
    """
    predefined_input = ['command', 'exit']
    input_index = 0

    def input_side_effect(prompt):
        nonlocal input_index
        if input_index < len(predefined_input):
            result = predefined_input[input_index]
            input_index += 1
            return result
        raise EOFError  # Simulate end of input

    with patch('builtins.input', side_effect=input_side_effect), \
            patch.object(app_instance.command_handler, 'execute_command') as mock_execute_command:
        app_instance.load_plugins()
        with pytest.raises(EOFError):  # Expect EOFError when input stream is closed
            app_instance.start()

        # Assert that the command is executed with the correct arguments
        expected_calls = [call('command', []), call('exit', [])]
        mock_execute_command.assert_has_calls(expected_calls)

    captured = capsys.readouterr()
    assert "Type 'exit' to exit." in captured.out
