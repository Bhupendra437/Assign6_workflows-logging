"""
Module containing unit tests for the main module.
"""

from unittest.mock import patch, Mock, call
from multiprocessing import Pool
import pytest
from main import main

def test_main_function():
    """
    Test the main function.
    """
    with patch('sys.argv', None), \
         patch('main.App') as mock_app, \
         patch('main.multiprocessing.Pool') as mock_pool, \
         patch('main.cpu_bound_task') as mock_cpu_bound_task:

        sample_data_list = [1, 2, 3]

        mock_cpu_bound_task.return_value = [10, 20, 30]

        main()

        mock_app_instance = mock_app.return_value
        mock_app_instance.start.assert_called_once()

        mock_pool_instance = mock_pool.return_value
        mock_pool_instance.map.assert_called_once_with(mock_cpu_bound_task, sample_data_list)

        mock_cpu_bound_task.assert_has_calls([call(1), call(2), call(3)])

        mock_pool_instance.close.assert_called_once()
        mock_pool_instance.join.assert_called_once()
