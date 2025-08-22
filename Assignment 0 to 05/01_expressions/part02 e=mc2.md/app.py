import random

NUM_SIDES = 6

def roll_dice():
    die1 : int = random.randint(1,NUM_SIDES)
    print("die1:" +  str(die1))
    die2 : int = random.randint(1,NUM_SIDES)
    print("die2:" +  str(die2))
    total : int = die1 + die2


    print("Total of two dice: ", total)

def main():
    die1 : int = 10
    print("die1 in main() start as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

    # This provided line is required at the end of a Python file
# to call the main() function.

if __name__ == '__main__':
    main()