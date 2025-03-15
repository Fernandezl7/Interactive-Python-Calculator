# app/plugins/History.py
import logging

from apps.commands import Command
from apps.commands import CommandHandler

class HistoryCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        logging.info(f"Invoked History Operation")
        print(self.command_handler.get_history())


def register(command_handler: CommandHandler):
    return HistoryCommand(command_handler)  # Return the class, not an instance
