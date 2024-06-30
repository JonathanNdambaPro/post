import pytest
from app.submodule_2.sub_app_2 import call_api


def test_call_api_valid(mock_url_valid):
    response = call_api(mock_url_valid)
    assert isinstance(response["fact"], str)
    assert isinstance(response["length"], int)


@pytest.mark.xfail(raises=ValueError)
def test_call_api_error_first_method_xfail(mock_url_no_valid):
    call_api(mock_url_no_valid)


def test_call_api_error_first_method_pytest(mock_url_no_valid):
    with pytest.raises(ValueError):
        call_api(mock_url_no_valid)
