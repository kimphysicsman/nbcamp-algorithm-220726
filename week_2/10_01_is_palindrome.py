input = "abcbcba"


def is_palindrome(string):
    for i in range(int(len(string)/2)):
        if string[i] != string[-(i+1)]:
            return False
    return True


print(is_palindrome(input))


def is_palindrome_recursion(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome_recursion(string[1:-1])
    else:
        return False


print(is_palindrome_recursion(input))