PROMPT: str = "What do you want? "
JOKE: str = "Why did the cookie go to the doctor?\nBecause it was feeling crummy! 🍪😆"
SORRY: str = "Sorry I only tell jokes."

def main():

    user_input = input(PROMPT).strip().lower()

    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()