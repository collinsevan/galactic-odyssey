from story import intro_story, prepare_ship_story, review_mission_story, final_challenge_story, mid_journey_check_story, unexpected_visitor_story
from health_manager import HealthManager

# Initialize health manager with 5 health points
health = HealthManager()

def start_game():
    print(intro_story())
    initial_choice()

def initial_choice():
    print("What will you do next?")
    print("1. Prepare the ship for launch")
    print("2. Review mission details")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        prepare_ship()
    elif choice == '2':
        review_mission()
    else:
        print("Invalid choice. Please select again.")
        initial_choice()

def prepare_ship():
    print(prepare_ship_story())
    health.reduce_health(1)
    print(f"Ship health: {health.get_health()}")
    mid_journey_check()

def review_mission():
    print(review_mission_story())
    mid_journey_check()

def mid_journey_check():
    print(mid_journey_check_story())
    print("1. Adjust shields to maximum")
    print("2. Ignore and continue on current course")
    print("3. Reroute to avoid the anomaly")
    
    choice = input("What's your command? (1, 2, or 3): ")
    if choice == '1':
        print("Shields enhanced, energy consumption increases but you're safer.")
        health.reduce_health(1)
    elif choice == '2':
        print("You take a risky gamble hoping the sensors are overreacting.")
    elif choice == '3':
        print("Course adjusted, this will add time but you avoid potential hazards.")
    else:
        print("Invalid choice. Please select again.")
        mid_journey_check()
    
    unexpected_visitor()

def unexpected_visitor():
    print(unexpected_visitor_story())
    print("1. Attempt to help the adrift vessel")
    print("2. Preserve resources and ignore the signal")
    print("3. Contact your command for instructions")
    
    choice = input("How do you respond? (1, 2, or 3): ")
    if choice == '1':
        print("You decide to help, using up resources but gaining potential allies.")
        health.reduce_health(2)
    elif choice == '2':
        print("You focus on your mission, ignoring the signal.")
    elif choice == '3':
        print("You wait for further instructions, delaying your mission slightly.")
    else:
        print("Invalid choice. Please select again.")
        unexpected_visitor()
    
    final_challenge()

def final_challenge():
    print(final_challenge_story())
    if health.get_health() > 2:
        print("You navigate the asteroid field successfully and your mission continues on course.")
    else:
        print("Your ship takes significant damage navigating through the asteroid field. Mission compromised.")
    end_game()

def end_game():
    if health.get_health() > 3:
        print("Congratulations! You've successfully launched the mission with your ship in good condition.")
    elif health.get_health() > 0:
        print("You barely manage to get your mission underway. It's going to be a challenging journey!")
    else:
        print("Unfortunately, the ship is too damaged to continue. Mission failed.")

if __name__ == "__main__":
    start_game()