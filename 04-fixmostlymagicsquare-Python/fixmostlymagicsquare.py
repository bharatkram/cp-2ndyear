# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.


def fixmostlymagicsquare(L):
    # Your code goes here
    row = -1
    column = -1
    diff = 0

    totals = []
    commonTotal = -1
    for row in L:
        total = sum(row)
        if total in totals:
            commonTotal = total
        totals.append(total)

    for i in range(len(L)):
        if sum(L[i]) != commonTotal:
            row = i
            diff = commonTotal - sum(L[i])
        col = []
        for j in range(len(L[0])):
            col.append(L[j][i])
        if sum(col) != commonTotal:
            column = i

    L[row][column] += diff
    return L
