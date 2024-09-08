from story import intro_story, prepare_ship_story, review_mission_story, final_challenge_story
from health_manager import HealthManager

# Initialize health manager with 5 health points
health = HealthManager()

def start_game():
    print(intro_story())
    print("What will you do next?")
    print("1. Prepare the ship for launch")
    print("2. Review mission details")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        prepare_ship()
    elif choice == '2':
        review_mission()
    else:
        print("Invalid choice. Please restart the game.")
        exit()

def prepare_ship():
    # Prepare ship and reduce health by 1 (simulating a malfunction)
    print("You are preparing the ship for launch, but an error occurred!")
    health.reduce_health(1)
    print(f"Ship health: {health.get_health()}")

def review_mission():
    # Review mission without affecting health
    print("You are reviewing the mission details. No issues detected.")

def final_challenge():
    # Describe the final challenge and determine the ending based on health
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