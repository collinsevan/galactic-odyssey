import os
from game_logic import start_game

def clear_screen():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome_message():
    clear_screen()
    print("=" * 80)
    print("Welcome to Galactic Odyssey".center(80))
    print("=" * 80)
    print("Press Enter to begin your space adventure...".center(80))
    input()
    clear_screen()

def print_help_message():
    clear_screen()
    print("=" * 80)
    print("Galactic Odyssey - Help Menu".center(80))
    print("=" * 80)
    print(
        "In Galactic Odyssey, you play as the captain of the spaceship *Starfire*. "
        "Your mission is to deliver critical supplies to the colony on Titan V. "
        "Throughout the journey, you'll face various challenges and make crucial "
        "decisions that affect the outcome of your mission."
    )
    print(
        "Here are some of the key elements you need to manage:"
    )
    print(
        "1. **Ship Health**: Your ship has a health meter that depletes when you face "
        "dangers or make poor decisions. Make sure to keep it above zero to continue."
    )
    print(
        "2. **Resources**: You'll need to manage resources carefully to avoid running out of "
        "essential supplies that can impact your mission."
    )
    print(
        "3. **Decisions**: At various points, you will be faced with choices that affect the "
        "outcome of your mission. Choose wisely to ensure the success of your journey."
    )
    print(
        "Press Enter to start the game."
    )
    input()
    clear_screen()

if __name__ == "__main__":
    # Start the game
    print_welcome_message()
    print_help_message()
    start_game()
