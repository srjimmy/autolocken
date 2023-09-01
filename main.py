import config
from src.runner import App
from src.utils.date import get_previous_weekdays

app = App(
    base_url=config.base_url,
    account=config.account,
    username=config.username,
    password=config.password,
    users=config.users,
    start_date=config.start_date if config.start_date else get_previous_weekdays()[0],
    end_date=config.end_date if config.end_date else get_previous_weekdays()[1],
    basename=config.basename,
)

if __name__ == "__main__":
    app.run()
