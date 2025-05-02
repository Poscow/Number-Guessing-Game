import random as rd

def intro():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Please select the difficulty level:\n")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

    while True:
        try:
            player_choice = int(input("Enter your choice (1-3): "))
            if player_choice == 1:
                return 10
            elif player_choice == 2:
                return 5
            elif player_choice == 3:
                return 3
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # rd_number = rd.randint(1, 100)
    rd_number = 30
    total_attempts = intro()
    print("\nLet's start the game!\n")

    attempts_used = 0

    while attempts_used < total_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        attempts_used += 1
        attempts_left = total_attempts - attempts_used

        if guess == rd_number:
            print(f"Congratulations! You guessed the correct number in {attempts_used} attempts.")
            break
        elif guess > rd_number:
            print(f"Incorrect! The number is less than {guess}.")
        else:
            print(f"Incorrect! The number is greater than {guess}.")

        if attempts_left > 0:
            print(f"You have {attempts_left} attempt(s) remaining.\n")
        else:
            print(f"\nSorry, you're out of guesses. The number was {rd_number}.")

main()
