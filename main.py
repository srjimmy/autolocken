import config
from src.runner import App
from src.utils.date import get_previous_weekdays

base_url: str = config.base_url
account: str = config.account
username: str = config.username
password: str = config.password
users: list[str] = config.users
start_date, end_date = get_previous_weekdays()
basename: str = config.basename

app = App(
    base_url=base_url,
    account=account,
    username=username,
    password=password,
    users=users,
    start_date=start_date,
    end_date=end_date,
    basename=basename,
)

if __name__ == "__main__":
    app.run()
