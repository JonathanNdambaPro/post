import pytest
from app.submodule_1.sub_app_1 import add_number
from app.submodule_2.sub_app_2 import call_api


def test_add():
    number_1 = 1
    number_2 = 2

    assert 3 == add_number(number_1, number_2)


def test_valid_call_api(mocker, mock_reponse_valid, mock_url_valid):
    with mocker.patch(
        "app.submodule_2.sub_app_2.requests.get", return_value=mock_reponse_valid
    ):
        response = call_api(mock_url_valid)

    assert response == {"lol": "lol"}


@pytest.mark.xfail(raises=ValueError)
def test_no_valid_call_api(mocker, mock_reponse_no_valid, mock_url_no_valid):
    with mocker.patch(
        "app.submodule_2.sub_app_2.requests.get", return_value=mock_reponse_no_valid
    ):
        call_api(mock_url_no_valid)
