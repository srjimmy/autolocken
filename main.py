import json
from src.runner import App
from src.utils.date import get_previous_weekdays

with open(file="config.json", mode="r") as config_file:
    config = json.load(fp=config_file)

base_url: str = config.get("base_url")
account: str = config.get("account")
username: str = config.get("username")
password: str = config.get("password")
users: list[str] = config.get("users")
start_date, end_date = get_previous_weekdays()
basename: str = config.get("basename")

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
