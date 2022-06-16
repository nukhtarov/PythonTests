import pytest
import allure
from clients.api_cleint import ApiClient


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    ('available', 1),
    pytest.param('sold', 10, id='sold test')
])
def test_3_up(state, expected):
    data = {
        "status": state
    }
    response = ApiClient().get_find_by_status(params=data).json()
    print(response)
