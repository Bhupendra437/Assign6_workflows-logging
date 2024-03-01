import pytest
from unittest.mock import patch, MagicMock
from app.plugins.calc.calculator import Calculator
from app.plugins.calc import CalcCommand

def test_execute_valid_args(capsys):
    # Instantiate CalcCommand
    calc_command = CalcCommand()
    # Mock the Calculator class
    with patch('app.plugins.calc.calculator.Calculator') as mock_calculator:
        # Mock the result of the calculator operation
        mock_calculator.add.return_value = 8
        # Execute the command
        calc_command.execute(['5', '3', 'add'])
        # Capture printed output
        captured = capsys.readouterr()
        # Assert the output is correct
        assert captured.out.strip() == "The result of 5 add 3 is equal to 8"

def test_execute_invalid_args(capsys):
    # Instantiate CalcCommand
    calc_command = CalcCommand()
    # Execute the command with invalid arguments
    calc_command.execute(['5', '3'])
    # Capture printed output
    captured = capsys.readouterr()
    # Assert the output is correct
    assert captured.out.strip() == "Usage: calc <number1> <number2> <operation>"

# Add more test cases to cover other scenarios
