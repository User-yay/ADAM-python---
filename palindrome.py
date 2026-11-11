def isPalindrome(string):
    Left_pos = 0
    Right_pos = len(string) - 1

    while Right_pos >= Left_pos:
        if not string [Left_pos] == string[Right_pos]:
            return False
        Left_pos += 1
        Right_pos -= 1
    return True

print("Is this a palindrome?")
print(isPalindrome("malayalam"))