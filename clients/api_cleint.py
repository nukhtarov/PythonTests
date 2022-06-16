import requests

from setting import URL, HEADERS


class ApiClient:

    def get_find_by_status(self, params, path="/v2/pet/findByStatus"):
        """

        :param params:
        :param path:
        :return:
        """

        response = requests.get(url=f'{URL}{path}',
                                headers=HEADERS,
                                params=params)
        response.raise_for_status()
        return response
