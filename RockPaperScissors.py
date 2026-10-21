import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
draws = 0
score_to_win = 3

while True:
    user_input = input("Rock, paper or scissors? ").strip().lower()

    if user_input in ["r", "rock"]:
        user_choice = "rock"
    elif user_input in ["p", "paper"]:
        user_choice = "paper"
    elif user_input in ["s", "scissors"]:
        user_choice = "scissors"
    else:
        print("Please choose rock, papper or scissors")
        continue

    print(f"\nYou chose: {user_choice}")
    
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("\nIt's a draw!")
        draws += 1
    elif (
        (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "rock" and computer_choice == "scissors")    
    ):
        user_score += 1
        print("\nYou win this round!")
    else:
        computer_score += 1
        print("\nThe computer wins this round!")

    print("\nScore:")
    print(f"You: {user_score}")
    print(f"The computer: {computer_score}")
    print(f"Draws: {draws}\n")

    if user_score == score_to_win or computer_score == score_to_win:
        break

print(f"\nFinal score:")
print(f"You: {user_score}")
print(f"The computer: {computer_score}")


if user_score > computer_score:
    print("\nCongratulations! You win!")
else:
    print("\nThe computer wins the game.")
