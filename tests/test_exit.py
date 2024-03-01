import pytest
import sys
from unittest.mock import patch
from app.plugins.exit import ExitCommand

def test_execute_exit():
    # Instantiate ExitCommand
    exit_command = ExitCommand()
    # Patch sys.exit to prevent actual exit
    with pytest.raises(SystemExit) as e:
        with patch.object(sys, 'exit') as mock_exit:
            # Execute the command
            exit_command.execute([])
    # Assert that sys.exit was called with the expected message
    assert str(e.value) == "Exiting..."
