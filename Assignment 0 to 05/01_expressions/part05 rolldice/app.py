# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES :int = 6

def main():
   # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)

    # Roll die
    # 1 (First Argument) → This is the minimum value, meaning the smallest number the dice can roll. Since a die has at least 1 on its face, we start from 1.
  # NUM_SIDES (Second Argument) → This is the maximum value, meaning the highest number the dice can roll. In this case, NUM_SIDES = 6, so the highest value is 6.
    die1 : int = random.randint(1,NUM_SIDES)
    die2 : int = random.randint(1,NUM_SIDES)

    # Get their total
    total: int = die1 + die2
    print("Diece have",NUM_SIDES,"sides each.")
    print("First die: ",die1)
    print("Second die: ",die2)
    print("Total of two dieceL: ",total)

if __name__ == '__main__':
  main()
     