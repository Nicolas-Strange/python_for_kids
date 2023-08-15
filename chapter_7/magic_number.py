import random


def guess_number() -> None:
    """
    Play a number guessing game where the player has to guess a secret number.

    The game continues until the player correctly guesses the number.

    Returns:
        None
    """
    secret_number: int = random.randint(1, 100)
    attempts: int = 0

    while True:
        try:
            guess: int = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                raise ValueError("Please enter a number between 1 and 100.")
        except ValueError as ve:
            print(ve)
            continue

        attempts += 1

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break


if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()
