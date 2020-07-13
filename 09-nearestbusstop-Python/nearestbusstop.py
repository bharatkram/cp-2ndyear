# Write the function nearestBusStop(street) that takes a
# non-negative int street number, and returns the nearest
# bus stop to the given street, where buses stop every 8th street,
# including street 0, and ties go to the lower street,
# so the nearest bus stop to 12th street is 8th street,
# and the nearest bus stop to 13 street is 16th street.
import math


def fun_nearestbusstop(street):
    return math.floor(street / 8) * 8 if (street / 8) - int(street / 8) <= 0.5 else math.ceil(street / 8) * 8
