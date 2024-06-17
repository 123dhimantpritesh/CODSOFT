import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user wins'
    else:
        return 'computer wins'

def play_game():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user wins':
            user_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("Computer wins!")
        print(f"Score - You: {user_score} Computer: {computer_score}")
        play_again = input("Do you want to play another round? (yes/no): ")
    print("Thanks for playing!")
play_game()