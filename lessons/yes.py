SECRET: int = 10

print("Im thinking of a number from 1-15.")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("YESSIRRRR")
else:
    print("Nah bro")
    if guess > SECRET:
        print("Too high brother")
    else:
        print("Too low brother")