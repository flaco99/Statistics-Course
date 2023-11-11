def is_palindrome(word):
    if len(word) < 2:  # base case
        return True
    elif word[0] != word[-1]:
        return False
    else:  # word[0]==word[-1] is true
        is_palindrome(word[1:-1])  # remove first and last char and see if middle is palindrome

print(is_palindrome('kayak'))