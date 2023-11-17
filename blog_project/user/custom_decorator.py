import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

file_handler = logging.FileHandler('uygulama.log')
logger.addHandler(file_handler)

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time

        log_message = f"{func.__name__} calisma suresi: {elapsed_time} saniye"

        logger.info(log_message)

        return result
    return wrapper