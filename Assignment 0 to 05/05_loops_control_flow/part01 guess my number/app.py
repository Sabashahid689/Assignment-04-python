import random

def main():
  # Generate the secret number at random!
  secret_number = random.randint(1,99)

  print("I am thinking number between 1 and 99.")

  guess = int(input("Enter your guess: "))
   # True if guess is not equal to secret number
  while guess != secret_number:
    if guess < secret_number:
      print("Your guess is to low ")
    else:
      print("Your guess is to high ")

      print()
    guess = int(input("Enter a new guess: "))

  print("congrats! The number was: " + str(secret_number))

if __name__ == "__main__":
  main()