import logging
import sys
from logging.handlers import TimedRotatingFileHandler

def setup_logger(name: str = "bot", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.hasHandlers():
        return logger

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    # File handler (rotate every midnight, keep only last file)
    file_handler = TimedRotatingFileHandler(
        "./logs/app.log",
        when="midnight",   # rotaciona à meia-noite
        interval=1,        # a cada 1 dia
        backupCount=1,     # mantém apenas 1 arquivo antigo
        encoding="utf-8"
    )
    file_handler.setFormatter(logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
