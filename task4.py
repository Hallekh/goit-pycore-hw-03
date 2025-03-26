from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime(2024, 1, 22).date()  # 👉 Фіксована дата для прикладу. Замінити на datetime.today().date() для реального використання
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday_raw = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Отримуємо дату дня народження на поточний рік
        birthday_this_year = birthday_raw.replace(year=today.year)

        # Якщо день народження вже був цього року — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Розрахунок кількості днів до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Якщо день народження в межах наступних 7 днів
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            # Якщо день народження на вихідних — переносимо на понеділок
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # Додаємо до списку
            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays



users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

result = get_upcoming_birthdays(users)
print(result)


