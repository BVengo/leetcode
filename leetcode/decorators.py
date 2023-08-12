import logging
import time

from functools import wraps

logging.basicConfig()
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)


def timed(func):
    """Prints the execution time for the decorated function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        end = time.time_ns()
        logger.debug(f"{func.__name__} ran in {end - start}ns")
        return result

    return wrapper