"""Examples of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list() #the function call list() is empty list

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# How to remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# How to sum the values of our rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i += 1

print(f"Total score: {sum}")


# How to access an individual item in a list
print(rolls[0])
print(rolls[1])

# How to access the length of a list
print(len(rolls))

# Using arithmetic to access last item of a list
last_index: int = len(rolls) - 1
print(rolls[last_index])