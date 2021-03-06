"""
The ``exceptions`` module houses custom exceptions. Currently implemented:

- OptimizationError
"""


class OptimizationError(Exception):
    """
    When an optimization routine fails – usually, this means
    that cvxpy has not returned the "optimal" flag.
    """

    def __init__(self, *args, **kwargs):
        default_message = "Please check your constraints or use a different solver."

        if not (args or kwargs):
            args = (default_message,)
        super().__init__(*args, **kwargs)
