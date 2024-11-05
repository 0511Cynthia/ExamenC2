def is_palindrome(string):
    cleaned_string = ''.join(string.split()).lower()
    return cleaned_string == cleaned_string[::-1]