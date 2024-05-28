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
    options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'], 
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['rock', 'scissors']
    }
    user_choice = input('Enter your choice: ').lower()
    if user_choice not in options:
        print('Invalid choice. Please try again.')
        rpls()
    comp_choice = random.choice(options)
    print(f'Computer choice: {comp_choice}')
    if user_choice == comp_choice:
        print('It\'s a tie!')
    elif comp_choice in rules[user_choice]:
        print('You win!')
    else:
        print('Computer wins!')

if __name__ == '__main__':
    rpls()

# Run the script
# Enter your choice: rock
# Computer choice: scissors

# Enter your choice: paper
# Computer choice: lizard

# Enter your choice: scissors
# Computer choice: spock






