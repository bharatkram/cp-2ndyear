# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"


def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    l1, l2 = len(s1), len(s2)
    l, pos = 0, -1

    c = [[-1]*(l2+1) for i in range(l1 + 1)]

    for i in range(l1 + 1):
        c[i][l2] = 0
    for j in range(l2):
        c[l1][j] = 0

    for i in range(l1 - 1, -1, -1):
        for j in range(l2):
            if s1[i] != s2[j]:
                c[i][j] = 0
            else:
                c[i][j] = 1 + c[i+1][j+1]
                if l < c[i][j]:
                    l = c[i][j]
                    pos = i

    return s1[pos: pos + l] if l > 0 else ""
