MINIMUM_HEIGHT : float = 4.5

def main():
  height = float(input("Enter your height: "))
  if height >= MINIMUM_HEIGHT:
     print("You're tall enough to ride!")
  else:
     print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
  main()