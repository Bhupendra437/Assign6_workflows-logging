"""
Unit tests for the ExitCommand class.
"""

import sys
from unittest.mock import patch
import pytest
from app.plugins.exit import ExitCommand

def test_execute_exit():
    """
    Test the execute method of ExitCommand.
    It should raise SystemExit with the expected message.
    """
    # Instantiate ExitCommand
    exit_command = ExitCommand()
    # Patch sys.exit to prevent actual exit
    with pytest.raises(SystemExit) as e:
        with patch.object(sys, 'exit'):
            # Execute the command
            exit_command.execute([])
    # Assert that sys.exit was called with the expected message
    assert str(e.value) == "Exiting..."
