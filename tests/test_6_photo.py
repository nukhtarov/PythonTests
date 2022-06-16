import allure
import pytest

from clients.api_cleint import ApiClient
from helpers.base_helper import get_filtered_animal_name


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    pytest.param('sold', 1, id='sold test'),
    pytest.param('available', 10, id='available test')
])
def test_6_photo(state, expected):
    """

    :param state:
    :param expected:
    :return:
    """
    data = {
        "status": state
    }
    pet_list = ApiClient().get_find_by_status(params=data).json()
    animal_with_filter = get_filtered_animal_name(pet_list)

    print(animal_with_filter)
    return animal_with_filter


