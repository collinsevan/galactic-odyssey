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

if __name__ == "__main__":
    # Start the game
    print_welcome_message()
    start_game()