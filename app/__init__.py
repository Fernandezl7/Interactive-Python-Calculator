import pkgutil
import importlib
import logging
import sys
from app.commands import CommandHandler
from app.commands import Command
import multiprocessing


class App:
    def __init__(self):
        """Initialize the App with a command handler and an empty plugin list."""
        self.command_handler = CommandHandler()
        self.plugins = []  # List to store the names of loaded plugins

    def load_plugins(self):
        """Dynamically load available plugins from the app.plugins package."""
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if plugin_name in ["menu", "history", "clearhistory", "deletehistory"]:
                            self.command_handler.register_command(plugin_name, item(self.command_handler))
                        else:
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # Ignore non-command items

    def start(self):
        """Run the application, process user input, and execute commands in a loop."""
        self.load_plugins()
        self.command_handler.execute_command("menu")

        while True:  # REPL (Read-Eval-Print Loop)
            choice = input("Choose an option: ").strip()

            try:
                if choice == 'C':
                    continue

                elif choice in ['add', 'subtract', 'multiply', 'divide']:
                    a = self.get_number("   Enter the first number: ")
                    b = self.get_number("   Enter the second number: ")

                    command = self.command_handler.load_plugin_register(choice, a, b)
                    if command:
                        command.execute()
                    else:
                        print(f"Error: Command '{choice}' not recognized.")

                elif choice in ['E', 'Exit']:
                    print("Exiting program...")
                    sys.exit()

                elif choice in ['greet', 'menu', 'history', 'llearhistory', 'deletehistory']:
                    result = self.command_handler.execute_command(choice)
                    if result:
                        print(result)
                    else:
                        print(f"Error: Command '{choice}' not found.")

                else:
                    print("Invalid option. Please try again.")

            except ZeroDivisionError:
                print("Error: Division by zero.")

            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

            print("\nType C : to Continue , Type E : to Exit")

    def get_number(self, prompt):
        """Helper function to get a valid float input from the user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

                
def start_app():
    """Start the application in a separate process."""
    apps = App()
    apps.start()


if __name__ == "__main__":
    multiprocessing.Process(target=start_app).start()
