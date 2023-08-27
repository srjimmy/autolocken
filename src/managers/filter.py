import requests
import json


class FilterManager:
    """
    A class for managing filtering operations for lockensmartaccess
    web application.

    Parameters:
        session (requests.Session): The authenticated session for making HTTP requests.
        url (str): The URL where filtering actions will be performed.
    """

    def __init__(self, session: requests.Session, url: str) -> None:
        self.session: requests.Session = session
        self.url: str = url

    def filter(self, users: list[str], start_date: str, end_date: str) -> None:
        """
        Apply filtering based on specified criteria.

        Parameters:
            users (list[str]): A list of usernames ids to filter data for.
            start_date (str): The start date of the filtering range.
            end_date (str): The end date of the filtering range.
        """
        payload: dict[str, str | list[str]] = {
            "advance_filter": "true",
            "count": "",
            "filter_criteria": "",
            "endUser[]": users,
            "eventDate": json.dumps(
                obj={"type": "STRETCH", "startDate": start_date, "endDate": end_date}
            ),
        }

        self.session.post(url=self.url, data=payload)
