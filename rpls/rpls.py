# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock
# - Rock crushes lizard
# - Lizard poisons Spock
# - Spock smashes scissors
# - Lizard eats paper
# - Paper disproves Spock
# - Spock vaporizes rock
# - Rock crushes scissors
# Include user input for selecting options and display game results
import random

def rpls():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    computer = random.choice(choices)
    user = input('Enter your choice: ')
    print(f'Computer choice: {computer}')

    if user == computer:
        print('It is a tie!')
    elif user == 'rock':
        if computer == 'scissors' or computer == 'lizard':
            print('You win!')
        else:
            print('You lose!')
    elif user == 'paper':
        if computer == 'rock' or computer == 'spock':
            print('You win!')
        else:
            print('You lose!')
    elif user == 'scissors':
        if computer == 'paper' or computer == 'lizard':
            print('You win!')
        else:
            print('You lose!')
    elif user == 'lizard':
        if computer == 'spock' or computer == 'paper':
            print('You win!')
        else:
            print('You lose!')
    elif user == 'spock':
        if computer == 'scissors' or computer == 'rock':
            print('You win!')
        else:
            print('You lose!')
    else:
        print('Invalid choice!')

if __name__ == '__main__':
    rpls()

# Run the script
# Enter your choice: rock
# Computer choice: scissors

# Enter your choice: paper
# Computer choice: lizard

# Enter your choice: scissors
# Computer choice: spock






