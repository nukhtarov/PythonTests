import requests
import pytest
from hamcrest import assert_that, greater_than
URL = "https://petstore.swagger.io"
ENDPOINT = "/v2/pet/findByStatus"


@pytest.mark.parametrize("state, expected", [
    ('available', 400),
    ('pending', 1),
    ('sold', 1)
])
def test_2_medium(state, expected):
    # CONDITION = "status=pending"
    CONDITION = {"status": f'{state}'}
    HEADERS = {'accept': 'application/json'}
    # swagger_url = f'{URL}{ENDPOINT}?{CONDITION}'
    swagger_url = f'{URL}{ENDPOINT}'

    # Arrange
    response = requests.get(url=swagger_url,
                            headers=HEADERS,
                            params=CONDITION)
    response.raise_for_status()

    pet_list = response.json()
    pet_count = len(pet_list)

    assert_that(
        actual=pet_count,
        matcher=greater_than(expected),
        reason=f'{pet_count} not more than expected {expected}'
    )