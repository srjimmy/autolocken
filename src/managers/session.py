import requests
from src.utils.logger import Logger


class SessionManager:
    """
    A class for managing sessions and authentication for lockensmartaccess
    web application.

    Parameters:
        url (str): The base URL of the web application.
        headers (dict[str, str]): Headers to be used for HTTP requests.
    """

    def __init__(self, url: str, headers: dict[str, str]) -> None:
        self.url: str = url
        self.headers: dict[str, str] = headers
        self.session = requests.Session()
        self.logger = Logger(name=__name__).logger

    def login(self, account: str, username: str, password: str) -> requests.Session:
        """
        Perform a login action using the provided credentials.

        Parameters:
            username (str): The username for authentication.
            password (str): The password for authentication.

        Returns:
            requests.Session: The authenticated session object.
        """
        payload: dict[str, str] = {
            "account": account,
            "login": username,
            "passwd": password,
            "cmd_login": "login",
            "account_name": "login",
            "uname": "",
            "email": "",
        }

        self.session.headers.update(self.headers)
        self.session.post(url=self.url, data=payload)

        return self.session
