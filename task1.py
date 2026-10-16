from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    try:
        # Try to convert the string to a datetime object
        # and extract the date without the time.
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        # Return a warning message if the string cannot be converted
        # to a datetime object.
        print(f"The date format is incorrect. Please enter the date in YYYY-MM-DD format.")
        return None

    # Gets the datetime object for the current date and
    # extract the date without the time.
    current_date = datetime.now().date()
    # Calculate the difference in days between the the current date and target date.
    # Return a positive value for past dates and a negative value for future dates.
    diff_date = current_date - target_date
    return diff_date.days

# Date in past.
print(get_days_from_today("2026-10-01"))
# Date in future.
print(get_days_from_today("2026-10-31"))
# Wrong date format.
print(get_days_from_today("2026-10-32"))
