"""
Unit tests for the CalcCommand class.
"""

from unittest.mock import patch
import pytest
from app.plugins.calc import CalcCommand

def test_execute_valid_args(capsys):
    """
    Test the execute method of CalcCommand with valid arguments.
    It should print the correct result.
    """
    # Instantiate CalcCommand
    calc_command = CalcCommand()
    # Mock the Calculator class
    with patch('app.plugins.calc.calculator.Calculator') as mock_calculator:
        # Configure the mock calculator to return a specific result for the add method
        mock_calculator.return_value.add.return_value = 8
        # Execute the command
        calc_command.execute(['5', '3', 'add'])
        # Capture printed output
        captured = capsys.readouterr()
        # Assert the output is correct
        expected_output = "The result of 5 add 3 is equal to 8"
        assert captured.out.strip() == expected_output

def test_execute_invalid_args(capsys):
    """
    Test the execute method of CalcCommand with invalid arguments.
    It should print a usage message.
    """
    # Instantiate CalcCommand
    calc_command = CalcCommand()
    # Execute the command with invalid arguments
    calc_command.execute(['5', '3'])
    # Capture printed output
    captured = capsys.readouterr()
    # Assert the output is correct
    assert captured.out.strip() == "Usage: calc <number1> <number2> <operation>"

# Add more test cases to cover other scenarios
