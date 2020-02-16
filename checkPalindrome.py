def checkPalindrome(inputString):
    my_str = inputString
    # make it suitable for caseless comparison
    my_str = my_str.casefold()
    # reverse the string
    rev_str = reversed(my_str)
    # check if the string is equal to its reverse
    if list(my_str) == list(rev_str):
        return  True
    else:
        return False

print(checkPalindrome("aabaa"))
print("- - - - -")
print(checkPalindrome("aaba"))
