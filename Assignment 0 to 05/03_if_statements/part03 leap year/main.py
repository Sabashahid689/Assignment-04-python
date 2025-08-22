def main():
  year : int = int(input("Enter a year: "))

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("That is a leap year.")
      else:
        print("That is not a leap year.")
    else:
      print("That is a leap year.")
  else:
    print("That is not a leap year.")

if __name__ == '__main__':
  main()