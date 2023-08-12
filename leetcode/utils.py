from importlib import import_module


def get_module(test_name: str):
    """
    Returns the corresponding module belonging to a test file.

    :param test_name: Extracted from a test file using __name__.
    """
    return import_module(f"leetcode.challenges.{test_name.replace('test', 'challenge')}")


def get_functions(test_name, function_name):
    """
    Returns all the version of the run functions from a challenge.

    :param name: The name of the test file, extracted using __name__.
    :param function_name: The name of the function to be tested (without _v#)
    """
    challenge = get_module(test_name)

    functions = [getattr(challenge, key) for key in challenge.__dict__.keys()
                 if key.startswith(function_name)]
    return functions
