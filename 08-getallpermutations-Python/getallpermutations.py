# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


def permutations(inp, i, l, result):
    if i == l:
        result.append(tuple(inp))
    else:
        for j in range(i, l):
            inp[i], inp[j] = inp[j], inp[i]
            permutations(inp, i + 1, l, result)
            inp[i], inp[j] = inp[j], inp[i]


def getallpermutations(x):
    # Your code goes here
    ret = []
    permutations(list(x), 0, len(x), ret)
    return sorted(ret)
