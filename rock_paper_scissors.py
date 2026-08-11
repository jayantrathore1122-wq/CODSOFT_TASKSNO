"""Task 4: Rock-Paper-Scissors Game"""

import random

CHOICES = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(CHOICES)


def get_user_choice():
    """Keep asking until the user enters a valid choice."""
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.\n")


def determine_winner(user, computer):
    """
    Return 'user', 'computer', or 'tie' based on classic RPS rules:
    Rock beats scissors, scissors beat paper, paper beats rock.
    """
    if user == computer:
        return "tie"

    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    if beats[user] == computer:
        return "user"
    else:
        return "computer"


def play_round(scores):
    """Play a single round and update the scores dictionary."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!\n")
    elif result == "user":
        print("You win this round!\n")
        scores["user"] += 1
    else:
        print("Computer wins this round!\n")
        scores["computer"] += 1


def show_scores(scores):
    print(f"Score -> You: {scores['user']}  |  Computer: {scores['computer']}\n")


def main():
    print("===== ROCK - PAPER - SCISSORS =====")
    print("Rules: Rock beats scissors, scissors beat paper, paper beats rock.\n")

    scores = {"user": 0, "computer": 0}

    while True:
        play_round(scores)
        show_scores(scores)

        again = input("Play another round? (y/n): ").strip().lower()
        if again != "y":
            print("\nFinal Score:")
            show_scores(scores)
            if scores["user"] > scores["computer"]:
                print("Congratulations, you won overall!")
            elif scores["user"] < scores["computer"]:
                print("Computer won overall. Better luck next time!")
            else:
                print("Overall, it's a tie!")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
