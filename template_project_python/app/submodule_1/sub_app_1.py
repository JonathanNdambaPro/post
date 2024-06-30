def add_number(number_1: int | float, number_2: int | float) -> int | float:
    """
    Calculate the sum of two numbers.

    Parameters
    ----------
    number_1 : int | float
        The first number to be added. Can be an integer or a float.
    number_2 : int | float
        The second number to be added. Can be an integer or a float.

    Returns
    -------
    int | float
        The sum of the two numbers. The return type will be float if any of the inputs is a float, otherwise it will be int.

    Examples
    --------
    >>> add_number(1, 2)
    3

    >>> add_number(1.5, 2.5)
    4.0

    >>> add_number(5, -3)
    2

    >>> add_number(2.3, 0.7)
    3.0
    """
    return number_1 + number_2
