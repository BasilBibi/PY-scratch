def is_palindrome(s):
    lower = s.lower()
    return lower == lower[::-1]