import requests
import pandas as pd


class ReportManager:
    """
    A class for managing the downloading of reports from lockensmartaccess
    web application.

    Parameters:
        session (requests.Session): The authenticated session for making HTTP requests.
        url (str): The URL where report download actions will be performed.
    """

    def __init__(self, session: requests.Session, url: str) -> None:
        self.session: requests.Session = session
        self.url: str = url

    def download(self, filename: str) -> None:
        """
        Download a report and save it to a file.

        Parameters:
            filename (str): The name of the file to save the downloaded report to.
        """
        payload: dict[str, str] = {
            "advance_filter": "true",
            "count": "",
            "filter_criteria": "",
        }

        response: requests.Response = self.session.post(url=self.url, data=payload)

        table_data: pd.DataFrame = pd.read_html(io=response.content)[0]
        table_data.to_excel(excel_writer=filename, index=False)
