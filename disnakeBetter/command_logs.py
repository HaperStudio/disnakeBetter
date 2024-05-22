"""

Copyright (C) 2024 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2024 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

import disnake
import logging
import os
import functools
from logging.handlers import RotatingFileHandler
from SpendScheme import Color

__all__ = [
    'LoggerCommands',
]

class LoggerCommands:
    
    """
    Disnake used commands in file logging.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Parameters
    ----------
    :param dir: Log file directory.
    :param dir: Log format.
    :param dir: Log with color.
    """

    def __init__(
            self,
            dir: str = r'logger\commands.txt',
            *,
            format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            color = None,
            mode: str = 'a',
            encoding: str = 'utf-8',
            maxBytes = 10**6,
            backupCount: int = 5

        ):

        self.formatter = logging.Formatter(format)
        commands_log_file = os.path.join(dir)

        self.color = color

        self.commands_handler = RotatingFileHandler(commands_log_file, mode = mode, encoding = encoding, maxBytes = maxBytes, backupCount = backupCount)
        self.commands_handler.setLevel(logging.INFO)
        self.commands_handler.setFormatter(self.formatter)

        self.commands_logger = logging.getLogger("commands_logger")
        self.commands_logger.setLevel(logging.INFO)
        self.commands_logger.addHandler(self.commands_handler)

    async def __log_command(self, inter: disnake.AppCmdInter):
        author = str(inter.author)
        command = str(inter.command)
        if self.slash:
            command = inter.data.name
        channel = str(inter.channel)
        guild = str(inter.guild)

        try:
            if self.color:
                author = Color.yellow + author + Color.end
                command = Color.yellow + command + Color.end
                channel = Color.yellow + channel + Color.end
                guild = Color.yellow + guild + Color.end
            
            log_text = f'"{author}" used command "{command}" in "{channel}" on server "{guild}"'
            self.commands_logger.info(log_text)

        except Exception as e:
            self.commands_logger.error(f"Error logging command: {e}")

    def command(self, slash = False) -> None:

        """
        Disnake used commands in file logging.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        Parameters
        ----------
        :param slash: If you use it with a slash command, you should specify True, if you use it with a normal command, then do not specify anything or specify False.
        """

        self.slash = slash

        def decorator(func):
            @functools.wraps(func)
            async def wrapper(inter: disnake.AppCmdInter, *args, **kwargs):
                try:
                    await self.__log_command(inter)
                    return await func(inter, *args, **kwargs)
                
                except Exception as e:
                    self.commands_logger.error(f"Error in slash command logger decorator: {e}")

            return wrapper
        return decorator