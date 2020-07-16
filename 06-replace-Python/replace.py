# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    # your code goes here
    pos, lenToBeReplaced, diff = 0, len(s2), len(s3) - len(s2)
    while pos <= len(s1):
        if s1[pos: pos + lenToBeReplaced + 1] == s2:
            s1 = s1[:pos] + s3 + s1[lenToBeReplaced + 1:]
            pos += diff
        else:
            pos += 1
    return s1
