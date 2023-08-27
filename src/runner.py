import requests
from src.managers.session import SessionManager
from src.managers.filter import FilterManager
from src.managers.report import ReportManager


class App:
    """
    A utility class to automate tasks related to accessing and managing data
    from lockensmartaccess web application.

    Parameters:
        base_url (str): The base URL of the lockensmartaccess web application.
        username (str): The username for authentication.
        password (str): The password for authentication.
        users (list[str]): A list of usernames to filter data for.
        start_date (str): The start date of the data range.
        end_date (str): The end date of the data range.
        basename (str): The basename of the report file.
    """

    def __init__(
        self,
        base_url: str,
        account: str,
        username: str,
        password: str,
        users: list[str],
        start_date: str,
        end_date: str,
        basename: str,
    ) -> None:
        self.base_url: str = base_url
        self.account: str = account
        self.username: str = username
        self.password: str = password
        self.users: list[str] = users
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.basename: str = basename

    def run(self) -> None:
        headers: dict[str, str] = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
        }

        session_Manager = SessionManager(url=self.base_url, headers=headers)
        login_session: requests.Session = session_Manager.login(
            account=self.account, username=self.username, password=self.password
        )

        filter_url: str = self.base_url + "AccessEvent-list.go"
        filter_Manager = FilterManager(session=login_session, url=filter_url)
        filter_Manager.filter(
            users=self.users, start_date=self.start_date, end_date=self.end_date
        )

        report_url: str = self.base_url + "AccessEvent-getExcelFile.go"
        report_Manager = ReportManager(session=login_session, url=report_url)
        filename: str = f"{self.basename} {self.start_date} a {self.end_date}.html"
        report_Manager.download(filename=filename)
