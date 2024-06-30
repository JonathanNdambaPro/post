from dataclasses import dataclass

import pytest


@pytest.fixture
def mock_url_valid():
    return "https://catfact.ninja/fact"


@pytest.fixture
def mock_url_no_valid():
    return "https://www.facebook.com/"


@pytest.fixture
def mock_reponse_valid():
    @dataclass
    class Response:
        status_code: int = 200

        def json(*_, **__):
            return {"lol": "lol"}

    response = Response()

    return response


@pytest.fixture
def mock_reponse_no_valid(mock_reponse_valid):
    mock_reponse_valid.status_code = 404
    return mock_reponse_valid
