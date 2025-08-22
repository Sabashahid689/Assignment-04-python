def main():
    print("This program will convert temperature from fahrenheit to celius ")
    fahrenheit  = float(input ("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32 )* 5.0 / 9.0 # formula which convert fahrenheit to celsius
    print(f"Temperature: {fahrenheit}F = {celsius}C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()