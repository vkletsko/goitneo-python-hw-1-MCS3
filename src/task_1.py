from datetime import datetime
from collections import defaultdict

birthday_dict = defaultdict(list)

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

def get_birthdays_per_week(users):
    current_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_current_year = birthday.replace(year=current_date.year)

        if birthday_current_year < current_date:
            birthday_current_year = birthday.replace(year=current_date.year + 1)

        delta_days = (birthday_current_year - current_date).days

        if delta_days < 7:
            if birthday_current_year.weekday() >= 5:
                birthday_dict[weekdays[0]].append(name)
            else:
                birthday_dict[weekdays[birthday_current_year.weekday()]].append(name)

    for day, users_list in birthday_dict.items():
        print(f"{day}: {', '.join(users_list)}")

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Linus Torvalds", "birthday": datetime(1969, 12, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Denzel Washington", "birthday": datetime(1954, 12, 28)},
    {"name": "Andrii Litun", "birthday": datetime(1980, 10, 13)},
    {"name": "Mario Bros", "birthday": datetime(2000, 10, 14)},
    {"name": "Bowser Jr.", "birthday": datetime(2010, 10, 14)},
    {"name": "Bowser", "birthday": datetime(1990, 10, 15)},
    {"name": "Princess Peach", "birthday": datetime(1985, 10, 16)},
    {"name": "Luigi", "birthday": datetime(1985, 10, 17)},
    {"name": "Donkey Kong", "birthday": datetime(1985, 10, 18)},
    {"name": "Yoshi", "birthday": datetime(1985, 10, 19)},
    {"name": "Toad", "birthday": datetime(1985, 10, 20)},
    {"name": "Goomba", "birthday": datetime(1985, 10, 21)},
    {"name": "Koopa Troopa", "birthday": datetime(1985, 10, 22)} 
]

if __name__ == "__main__":
    get_birthdays_per_week(users)