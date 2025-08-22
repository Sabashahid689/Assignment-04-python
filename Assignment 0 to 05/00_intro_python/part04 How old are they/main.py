def main():
    print("In this program will solve age-related riddle!\n")
    aton : int = 21 # Anton's age is given as 21 years old
    beth : int = aton + 6 # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen : int = beth + 20 # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew : int = chen + aton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan :int = chen # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

    # Print out all of the ages!
    print("\t \t Aton is " + str(aton))
    print("\t \t Beth is " + str(beth))
    print("\t \t Chen is " + str(chen))
    print("\t \t Drew is " + str(drew))
    print("\t \t Ethan is " + str(ethan))

# This provided line is required at the end of
# Python file to call the main() function.

if __name__ == '__main__':
    main()
     