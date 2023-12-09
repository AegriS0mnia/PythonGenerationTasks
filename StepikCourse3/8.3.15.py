def is_palindrome(word, i=0):
    if i == len(word) // 2:
        return True
    if word[i] != word[len(word) - 1 - i]:
        return False
    else:
        return is_palindrome(word, i + 1)

