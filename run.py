import os
import sys
from game_logic import start_game
from utils import format_output


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_welcome_message():
    """Display the welcome message and wait for user input."""
    clear_screen()
    print("=" * 80)
    print(
        format_output("Welcome to Galactic Odyssey", width=55)
        .center(80)
    )
    print("=" * 80)
    print(
        format_output(
            "Press Enter to begin your space adventure...", width=55
        ).center(80)
    )
    print(
        format_output("Press 'h' for help at any time.", width=55)
        .center(80)
    )
    choice = input().strip().lower()
    if choice == 'h':
        print_help_message()
    else:
        clear_screen()


def print_help_message():
    """Display the help message and wait for user input."""
    clear_screen()
    print("=" * 80)
    print(
        format_output("Galactic Odyssey - Help Menu", width=55).center(80)
    )
    print("=" * 80)
    help_text = (
        "In Galactic Odyssey, you play as the captain of the spaceship "
        "*Starfire*. Your mission is to deliver critical supplies to the "
        "colony on Titan V. Throughout the journey, you'll face various "
        "challenges and make crucial decisions that impact your mission’s "
        "outcome.\n\n"
        "Key elements to manage:\n"
        "1. **Ship Health**: Your ship has a health meter that depletes with "
        "dangers or poor decisions. Keep it above zero to continue.\n"
        "2. **Resources**: Manage resources carefully to avoid running out "
        "of essential supplies, which impacts your mission.\n"
        "3. **Decisions**: Make choices that affect the mission’s outcome. "
        "Choose wisely to ensure success.\n\n"
        "Press Enter to start the game."
    )
    print(format_output(help_text, width=55))
    input()
    clear_screen()


if __name__ == "__main__":
    # Start the game
    print_welcome_message()
    start_game()