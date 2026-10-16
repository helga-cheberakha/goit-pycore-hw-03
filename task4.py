from datetime import datetime, timedelta

# Get the user birthday for the year.
def get_birthday_for_year(birthday: datetime, year: int) -> datetime:
    try:
        return birthday.replace(year=year)
    except (ValueError):
        # Use March 1 for leap-day birthdays in non-leap years.
        return birthday.replace(year=year, month=3, day=1)

# Add today as a parameter to the method for testing purposes. 
def get_upcoming_birthdays(users: list, today: datetime | None = None) -> list:
    # Get the current date as a date without time.
    if today is None:
        today = datetime.now().date()

    # Build list of users upcoming birthdays.
    upcoming_birthdays = []

    for user in users:
        # Get a date object without time for the user birthday str.
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

        # Get the user birthday to the current year.
        birthday_current_year = get_birthday_for_year(birthday, today.year)

        # Get the user birthday to the next year if it has already passed
        # for the current year.
        if birthday_current_year < today:
            birthday_current_year = get_birthday_for_year(birthday, today.year + 1)

        # Get the difference in days.
        days_until_birthday = (birthday_current_year - today).days

        # Check whether the user birthday is within the next 7 days.
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_current_year

            # Check whether the user birthday is on weekend
            # and move it to the Monday
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Add the user birthday to the result list.
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alex Brown", "birthday": "1972.10.18"},
    {'name': 'Anna White', 'birthday': '1992.10.20'},
    {'name': 'Mike Green', 'birthday': '1988.10.21'},
    {'name': 'Stuart Grey', 'birthday': '1988.10.24'},
    {'name': 'Richard Garison', 'birthday': '1996.02.29'}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print('Upcoming birthdays:', upcoming_birthdays)

# Test leap and non-leap years.
# Non-leap year.
non_leap_current_date = datetime(2027, 2, 25).date()
non_leap_upcoming_birthdays = get_upcoming_birthdays(users,  non_leap_current_date)
print('Current date:', non_leap_current_date)
print('Upcoming birthdays:', non_leap_upcoming_birthdays)

# Leap year.
leap_current_date = datetime(2028, 2, 25).date()
leap_upcoming_birthdays = get_upcoming_birthdays(users,  leap_current_date)
print('Current date:', leap_current_date)
print('Upcoming birthdays:', leap_upcoming_birthdays)
