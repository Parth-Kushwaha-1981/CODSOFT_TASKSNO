import random

print("Rock-Paper-Scissors Game")
print("------------------------")

while True:
    print("\nChoose:")
    print("R - Rock")
    print("P - Paper")
    print("S - Scissors")

    user_choice = input("Enter your choice: ").upper()

    if user_choice not in ["R", "P", "S"]:
        print("Invalid choice. Please choose R, P, or S.")
        continue

    computer_choice = random.choice(["R", "P", "S"])

    print("Your choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P"):
        print("You win!")

    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (Y/N): ").upper()

    if play_again != "Y":
        print("Thanks for playing!")
        break
