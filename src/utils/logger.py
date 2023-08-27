import logging


class Logger:
    """
    A utility class for configuring and using a logging system in the application.

    Parameters:
        name (str): The name to be associated with the logger.
    """

    def __init__(self, name: str) -> None:
        self.logger: logging.Logger = logging.getLogger(name=name)
        self.logger.setLevel(level=logging.INFO)

        file_handler = logging.FileHandler(filename="locken.log")
        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(fmt=formatter)

        self.logger.addHandler(hdlr=file_handler)
