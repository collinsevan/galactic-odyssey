from story import intro_story, prepare_ship_story, review_mission_story, final_challenge_story, system_check_story, crew_briefing_story
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
    system_check()

def review_mission():
    print(review_mission_story())
    system_check()

def system_check():
    print(system_check_story())
    print("1. Check engine status")
    print("2. Inspect cargo hold")
    print("3. Test communication systems")
    
    choice = input("Make your choice (1, 2, or 3): ")
    
    if choice == '1':
        print("Engine status is optimal.")
    elif choice == '2':
        print("Cargo hold is secure.")
    elif choice == '3':
        print("Communication systems are functional.")
    else:
        print("Invalid choice. Please select again.")
        system_check()
    
    crew_briefing()

def crew_briefing():
    print(crew_briefing_story())
    print("1. Motivate the crew")
    print("2. Discuss potential risks")
    print("3. Outline mission objectives")
    
    choice = input("How will you brief your crew? (1, 2, or 3): ")
    
    if choice == '1':
        print("The crew feels motivated and ready.")
    elif choice == '2':
        print("The crew is now aware of potential risks.")
    elif choice == '3':
        print("Mission objectives are clear to everyone.")
    else:
        print("Invalid choice. Please select again.")
        crew_briefing()
    
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