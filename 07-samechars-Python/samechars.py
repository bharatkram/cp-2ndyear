# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either
# parameter is not a string, but returns True if both strings are empty (why?).


def samechars(tup):
    # Your code goes here
    if not isinstance(tup[0], str) or not isinstance(tup[1], str):
        return False
    s1, s2 = sorted(list(tup), key=lambda x: len(x))

    s1Dict = {}
    for char in s1:
        s1Dict[char] = True

    for char in s2:
        try:
            check = s1Dict[char]
        except KeyError:
            return False

    return True
