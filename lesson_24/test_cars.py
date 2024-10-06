import pytest
from requests import Session
from assertpy import assert_that
from requests import Response
from requests.auth import HTTPBasicAuth
import logging

BASE_URL: str = "http://127.0.0.1:8080"

logging.basicConfig(filename='test_search.log', level=logging.INFO)


@pytest.fixture(scope="session", autouse=True)
def authorization() -> Session:
    """
    Fixture for authorization of a client. Rotates a session with an authorization token.
    """
    auth = HTTPBasicAuth('test_user', 'test_pass')

    try:
        response: Response = Session().post(f"{BASE_URL}/auth", auth=auth)
        response.raise_for_status()
    except Exception as e:
        logging.error(f"Failed to authenticate: {e}")
        pytest.fail("Failed to authenticate")

    assert_that(response.status_code).is_equal_to(200)
    access_token: str = response.json().get("access_token")

    current_session = Session()
    current_session.headers.update({'Authorization': 'Bearer ' + access_token})

    logging.info("Authenticated successfully")
    return current_session


class TestAuthorization:

    def test_authorization_success(self, authorization: Session):
        """
        Verifies that the authorization process is successful.
        """
        logging.info("Authorization successful. Session obtained.")
        assert_that(authorization.headers).contains_key('Authorization')


class TestCarAPI:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 10),
        ("brand", 15),
        ("engine_volume", 20),
        (None, 25),
    ])
    def test_get_cars(self, authorization: Session, sort_by, limit):
        """
        Checks the search for cars with different sorting and delineation parameters.
        """
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logging.info(f"Testing GET /cars with sort_by={sort_by} and limit={limit}")

        try:
            response: Response = authorization.get(f"{BASE_URL}/cars", params=params)
            response.raise_for_status()
        except Exception as e:
            logging.error(f"Failed to get cars: {e}")
            pytest.fail("Failed to get cars")

        assert response.status_code == 200
        assert isinstance(response.json(), list)
        if limit:
            assert len(response.json()) == limit
