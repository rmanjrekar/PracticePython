"""
A palindrome is a word, phrase, number, or sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization in some cases.
"""

import re
"""
Steps:
    1. remove the spaces and other special characters and make it to lower case
    2. check if reverse cleaned string and cleaned string is same
"""

def reverse_string(input_str):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', input_str).lower()
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False

"""
Steps: Two pointer approach
    1. remove the spaces and other special characters and make it to lower case
    2. set start and end pointers to 0 and last index
    3. loops till start is less than equal
        check if start index element is same as left index element
        if not same, return False - not a palindrome
        if it is same, add start by 1 and subtract end by 1
"""

def two_pointer_approach(input_str):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', input_str).lower()
    start, end = 0, len(cleaned)-1

    while start <= end:
        if cleaned[start] != cleaned[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

assert two_pointer_approach("A man, a plan, a canal, Panama!") == True
assert two_pointer_approach("Racecar") == True
assert two_pointer_approach("12321") == True
assert two_pointer_approach("Palindrome") == False
assert reverse_string("Madam") == True
assert reverse_string("Not a palindrome") == False
assert reverse_string("Was it a car or a cat I saw?") == True
assert reverse_string("12345") == False
