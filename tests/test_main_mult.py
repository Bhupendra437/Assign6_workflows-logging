import pytest
from unittest.mock import patch, Mock, call
from multiprocessing import Pool

# Import main function from your script
from main import main

def test_main_function():
    # Mocking sys.argv to pass None as args
    with patch('sys.argv', None):
        # Mocking the App class and its start method
        with patch('main.App') as mock_app:
            # Mocking the multiprocessing.Pool class and its methods
            with patch('main.multiprocessing.Pool') as mock_pool:
                # Mocking the cpu_bound_task function
                with patch('main.cpu_bound_task') as mock_cpu_bound_task:
                    # Define some sample data list
                    sample_data_list = [1, 2, 3]

                    # Mock the return value of cpu_bound_task
                    mock_cpu_bound_task.return_value = [10, 20, 30]

                    # Call the main function
                    main()

                    # Assert that App is instantiated correctly and its start method is called
                    mock_app_instance = mock_app.return_value
                    mock_app_instance.start.assert_called_once()

                    # Assert that multiprocessing.Pool is created with the correct number of processes
                    mock_pool_instance = mock_pool.return_value
                    mock_pool_instance.map.assert_called_once_with(mock_cpu_bound_task, sample_data_list)

                    # Assert that cpu_bound_task is called with each item in sample_data_list
                    mock_cpu_bound_task.assert_has_calls([call(1), call(2), call(3)])

                    # Assert that the multiprocessing pool is closed and joined properly
                    mock_pool_instance.close.assert_called_once()
                    mock_pool_instance.join.assert_called_once()
