import logging

from os import environ
from logging import Logger
from logging.handlers import RotatingFileHandler
from colorama import Fore, Style, init


init(autoreset=True)

class CustomFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT,
    }

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelno, "")
        record.levelname = f"{color}{record.levelname}{Style.RESET_ALL}"
        return super().format(record)


def get_logger(name: str = "default_logger", logglevel: int = logging.INFO) -> Logger:
    logger = logging.getLogger(name)
    if environ.get('DEBUG'):
        logglevel =  logging.DEBUG
    logger.setLevel(logglevel)

    file_handler = RotatingFileHandler(
        "logs/backend_app.log",
        maxBytes=50*1024*1024,
        backupCount=3
    )

    console_handler = logging.StreamHandler()

    formatter = CustomFormatter(
        fmt="%(asctime)s - %(filename)s line:%(lineno)d - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S "
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
