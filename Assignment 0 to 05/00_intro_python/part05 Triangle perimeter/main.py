def main():
    # get the 3 side length of triangle
    side_01 : float = float(input("Enter the length of side 1? "))
    side_02 : float = float(input("Enter the length of side 2? "))
    side_03 : float = float(input("Enter the length of side 3? "))

    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print("The parimeters of triangle is: " + str(side_01 + side_02 + side_03))

# This provided line is required at the end of
# Python file to call the main() function.
if  __name__ == '__main__':
    main()



