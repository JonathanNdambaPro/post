import requests


def call_api(url: str) -> dict[str, str]:
    """
    Send a GET request to the specified URL and return the JSON response.

    Parameters
    ----------
    url : str
        The URL to which the GET request is sent.

    Returns
    -------
    dict[str, str]
        A dictionary containing the parsed JSON data if the request is successful.
        If the request fails, returns a dictionary with an 'error' key and a 'status_code' key,
        detailing the type of error and the HTTP status code.

    Examples
    --------
    Successful request example:
    >>> call_api('https://api.example.com/data')
    {'key': 'value', 'another_key': 'another_value'}

    Failed request example:
    >>> call_api('https://api.example.com/bad_endpoint')
    {'error': 'Failed to fetch data', 'status_code': 404}
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        message_error = f"Some error in the call : {response.status_code}"
        raise ValueError(message_error)
