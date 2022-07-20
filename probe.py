def is_palindrome(text):
    text = text.lower()
    a = [c for c in text if c.isalpha()]
    return a == a[::-1]

txt = input()

print(is_palindrome(txt))