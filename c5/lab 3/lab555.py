import random

print("DICE SIMULATOR")

rolls = int(input("How many times do you want to roll? "))

for i in range(rolls):

    dice = random.randint(1, 6)

    print("Roll", i + 1, ":", dice)