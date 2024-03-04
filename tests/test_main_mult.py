"""Module for testing the main function with multiprocessing."""

from unittest.mock import patch
import main

def test_main_function():
    """Test the main function with mocked multiprocessing and App components."""
    with patch('main.App') as mock_app, \
         patch('main.multiprocessing.cpu_count', return_value=3), \
         patch('main.multiprocessing.Pool') as mock_pool, \
         patch('main.cpu_bound_task') as mock_cpu_bound_task:

        # Define the data list to be passed to the cpu_bound_task function
        your_data_list = [1, 2, 3]

        # Set the return value for the cpu_bound_task function
        mock_cpu_bound_task.return_value = 10

        # Call the main function
        main.main()

        # Assert that the App class was instantiated and started
        mock_app.assert_called_once()
        mock_app_instance = mock_app.return_value
        mock_app_instance.start.assert_called_once()

        # Assert that the Pool was created with the correct number of processes
        mock_pool.assert_called_once_with(processes=3)

        # Get the instance of the Pool mock and assert that the map method was called correctly
        mock_pool_instance = mock_pool.return_value.__enter__.return_value
        mock_pool_instance.map.assert_called_once_with(main.cpu_bound_task, your_data_list)
