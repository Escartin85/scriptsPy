# imports
import itertools

for x in itertools.count(50):
    print(x)
    if x == 80:
        break

for c in itertools.cycle("RACECAR"):
    print(c)
    if c == 'E':
        break


election = {1: "Barb",  2:"Karen",  3:"Erin"}

# Permutations: Order matters - some copies with same inputs but in different order
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)

# Combinations: Order does not matter - no copies with same inputs
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]

for c in itertools.combinations(colorsForPainting, 2):
    print(c)
