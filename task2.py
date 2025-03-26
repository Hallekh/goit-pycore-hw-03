import random

def get_numbers_ticket(min, max, quantity):
    # Checking if the input parameters are valid
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Generate unique random numbers within the given range
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    
    # Return the sorted list of numbers
    return sorted(lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)
