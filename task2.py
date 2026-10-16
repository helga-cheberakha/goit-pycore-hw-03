import random

def get_numbers_ticket(min: int, max: input, quantity: int) -> list:
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        print('All parameters must be integers')
        return []

    if min < 1:
        print('Minimum number must be 1 or greater')
        return []

    if max > 1000:
        print('Maximum number must be 1000 or less')
        return []

    if min > max:
        print('Minimum number must be less than maximum number')
        return []

    if quantity < 1 or quantity > max - min + 1:
        print(f'Invalid quantity of numbers. It must be between 1 and {max - min + 1}')
        return []

    # Generate unique random numbers.
    random_numbers = range(min, max + 1)
    result_numbers = random.sample(random_numbers, quantity)

    # Return sorted list of numbers.
    return sorted(result_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print('Your lottery numbers:', lottery_numbers)

lottery_numbers = get_numbers_ticket(-1, 49, 6)
print('Your lottery numbers:', lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 1001, 6)
print('Your lottery numbers:', lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 51)
print('Your lottery numbers:', lottery_numbers)

    