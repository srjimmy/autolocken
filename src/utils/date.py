from datetime import datetime, timedelta


def get_previous_weekdays() -> tuple[str, str]:
    """
    Calculate the dates of the previous week's Monday and Friday.

    Returns:
        tuple[str, str]: A tuple containing the formatted strings of the Monday
                         and Friday dates in the format "YYYY-MM-DD".
    """
    today: datetime = datetime.today()
    days_to_monday: int = today.weekday() + 7

    prev_monday: datetime = today - timedelta(days=days_to_monday)
    prev_friday: datetime = prev_monday + timedelta(days=4)

    fmt_prev_monday: str = prev_monday.strftime("%Y-%m-%d")
    fmt_prev_friday: str = prev_friday.strftime("%Y-%m-%d")

    return fmt_prev_monday, fmt_prev_friday
