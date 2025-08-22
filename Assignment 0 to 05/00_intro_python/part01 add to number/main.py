def main():
    print("This program add two numbers.")
    num1 : str = input("Enter First number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter Second number: ")
    num2 : int = int(num2)
    total : int = num1 + num2
    print("The total is: " + str(total) +".")

  # This provided line is required at the end of
  # Python file to call the main() function.
if __name__ == '__main__':
  main()