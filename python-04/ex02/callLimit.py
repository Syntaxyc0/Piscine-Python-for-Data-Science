from typing import Any

def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        """
        function that sets a limit of use to a certain limit for a given function
        """
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function

    return callLimiter