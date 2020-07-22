# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
    # your code goes here
    ret = 0
    mul = 0
    while x > 0 or y > 0:
        dig1 = x % 10**mul
        dig2 = y % 10**mul
        ret += ((dig1+dig2) % 10) * 10**mul
        mul += 1
    return ret + x * 10**mul if x > 0 else ret + y * 10**mul
