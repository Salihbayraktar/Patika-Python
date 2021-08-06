import sys


def cakes(recipe, available):
    availableCake = sys.maxsize
    for i in recipe:
        try:
            if availableCake > available[i] // recipe[i]:
                availableCake = available[i] // recipe[i]
        except KeyError:
            return 0
    return availableCake
