from datetime import datetime

def days_between(start_date: str, end_date: str) -> int:
    fmt = "%Y-%m-%d"
    return (datetime.strptime(end_date, fmt) - datetime.strptime(start_date, fmt)).days + 1

