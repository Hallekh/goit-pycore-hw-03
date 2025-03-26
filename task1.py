from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert the input string into a datetime object
        given_date = datetime.strptime(date, "%Y-%m-%d")
        # Get the current date
        today = datetime.today()
        # Calculate the difference in days
        delta = (given_date - today).days
        return delta
    except ValueError:
        # Handle error if the date format is incorrect
        return "Invalid date format. Please use 'YYYY-MM-DD' format."


result = get_days_from_today("2016-04-10")
print(result)
