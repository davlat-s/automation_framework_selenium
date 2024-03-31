import logging
import datetime

now = datetime.datetime.now()
LOG_FILE_PATH = f'./logs/selenium_log_{now}.log'


class LogGen:

    @staticmethod
    def loggen():
        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Create a file handler
        now = datetime.datetime.now()
        file_handler = logging.FileHandler(LOG_FILE_PATH)
        file_handler.setLevel(logging.INFO)

        # Set the format for the file handler
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)

        # Get the root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        # Add the file handler to the root logger
        root_logger.addHandler(file_handler)

        return root_logger

