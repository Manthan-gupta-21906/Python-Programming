def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

t = input("Enter a string: ")

if palindrome(t):
    print("is palindrome")
else:
    print("is not palindrome")