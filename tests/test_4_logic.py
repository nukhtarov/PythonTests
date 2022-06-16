import allure
import pytest

from clients.api_cleint import ApiClient


@allure.title('Test title')
@pytest.mark.parametrize("state, expected", [
    pytest.param('sold', 1, id='sold test'),
    pytest.param('available', 10, id='available test')
])
def test_4_logic(state, expected):
    """

    :param state:
    :param expected:
    :return:
    """
    data = {
        "status": state
    }
    pet_list = ApiClient().get_find_by_status(params=data).json()

    count = list()
    for pet in pet_list:
        category = pet.get('category', None)
        if category and "string" not in category.get('name'):
            count.append(category.get('name'))
    print(count)
    return count
