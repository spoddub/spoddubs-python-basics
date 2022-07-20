def is_palindrome(text):
    text = text.lower()
    a = [c for c in text if c.isalpha()]
    return a == a[::-1]


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def is_even(num):
    return num % 2 == 0


def is_valid_password(password):
    return is_even() and