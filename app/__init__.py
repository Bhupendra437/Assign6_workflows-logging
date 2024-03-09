import pkgutil
import importlib
import logging
import os
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand
import logging.config

class App:
    """
    The main application class responsible for loading plugins and executing commands.
    """

    class ExitApplication(Exception):
        """Custom exception for exiting the application."""
        pass

    class TestInputEnd(Exception):
        """Exception to signal the end of input in tests."""
        pass

    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """
        Load plugins dynamically from the app.plugins package.
        """
        plugins_package = 'app.plugins'
        try:
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if isinstance(item, type) and issubclass(item, Command) and item != Command:
                                command_name = getattr(item, 'name', item.__name__.lower())
                                self.command_handler.register_command(command_name, item())
                        except TypeError:
                            continue
        except Exception as e:
            logging.error(f"Error loading plugins: {e}")

    def start(self):
        """
        Start the application by loading plugins and registering commands.
        """
        self.load_plugins()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        logging.info("Type 'exit' to exit.")
        while True:
            try:
                user_input = input(">>> ").strip().split()
                if user_input:
                    command = user_input[0].lower()
                    args = user_input[1:]
                    logging.debug(f"Received command: {command} with args: {args}")
                    self.command_handler.execute_command(command, args)
            except App.ExitApplication:
                break
            except Exception as e:
                logging.error(f"Error executing command: {e}")
