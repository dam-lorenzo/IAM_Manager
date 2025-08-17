import sys
from .utils.logger import get_logger

logger = get_logger()

def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Ctrl+C without logging
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical(
        "Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )

sys.excepthook = log_uncaught_exceptions