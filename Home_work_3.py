from datetime import datetime, timedelta

users = []

def get_birthdays_per_week(users):
    today = datetime.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthday_dict = {day: [] for day in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=today.year)
        day = birthday.strftime('%A')
        if day == 'Saturday':
            day = 'Monday'
            birthday += timedelta(days=2)
        elif day == 'Sunday':
            day = 'Monday'
            birthday += timedelta(days=1)
        if today <= birthday <= today + timedelta(days=7):
            birthday_dict[day].append(name)

    for day, names in birthday_dict.items():
        if names:
            print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(users)