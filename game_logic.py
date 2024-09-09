from story import (
    intro_story,
    prepare_ship_story,
    review_mission_story,
    equipment_malfunction_story,
    mid_journey_check_story,
    critical_meltdown_story,
    advanced_medical_facility_story,
    alien_encounter_story,
    resource_dilemma_story,
    unexpected_visitor_story,
    final_challenge_story
)
from health_manager import HealthManager
health = HealthManager()  # Initialize health manager with 5 health points

def start_game():
    print(intro_story())
    initial_choice()

def initial_choice():
    while True:
        print("What will you do next?")
        print("1. Prepare the ship for launch")
        print("2. Review mission details")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            prepare_ship()
            break
        elif choice == '2':
            review_mission()
            break
        else:
            print("Invalid choice. Please select again.")

def prepare_ship():
    print(prepare_ship_story())
    health.reduce_health(1)
    print(f"Ship health: {health.get_health()}")
    equipment_malfunction()

def review_mission():
    print(review_mission_story())
    equipment_malfunction()

def equipment_malfunction():
    print(equipment_malfunction_story())
    while True:
        print("1. Repair the life support system using spare parts")
        print("2. Attempt a manual fix without using resources")
        choice = input("Choose your action (1 or 2): ")
        if choice == '1':
            print("You've successfully repaired the system and conserved oxygen.")
            health.gain_health(1)
            break
        elif choice == '2':
            print("The manual fix failed, further straining the life support.")
            health.reduce_health(1)
            break
        else:
            print("Invalid choice. Please select again.")
    mid_journey_check()

def mid_journey_check():
    print(mid_journey_check_story())
    while True:
        print("1. Adjust shields to maximum")
        print("2. Ignore and continue on current course")
        print("3. Reroute to avoid the anomaly")
        choice = input("What's your command? (1, 2, or 3): ")
        if choice == '1':
            print("Shields enhanced, energy consumption increases but you're safer.")
            health.reduce_health(1)
            break
        elif choice == '2':
            print("You take a risky gamble hoping the sensors are overreacting.")
            break
        elif choice == '3':
            print("Course adjusted, this will add time but you avoid potential hazards.")
            break
        else:
            print("Invalid choice. Please select again.")

    critical_meltdown()

def critical_meltdown():
    print(critical_meltdown_story())
    print("1. Attempt to stabilize the reactor")
    print("2. Abandon the reactor and evacuate")
    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print("You manage to stabilize the reactor, but the ship's systems are severely compromised.")
        health.reduce_health(3)
        if health.get_health() <= 0:
            end_game()
            return
    elif choice == '2':
        print("Evacuation is successful, but your ship suffers irreversible damage.")
        health.reduce_health(2)
    else:
        print("Invalid choice. Please select again.")
        critical_meltdown()
    advanced_medical_facility()

def advanced_medical_facility():
    print(advanced_medical_facility_story())
    print("1. Integrate the health systems with your ship")
    print("2. Leave the facility and continue the mission")
    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print("The integration is successful. Your ship's maximum health is increased and current health is fully restored.")
        health.set_max_health(10)  # Assuming a new method to set max health
        health.restore_health()
    elif choice == '2':
        print("You continue the mission without any enhancements.")
    else:
        print("Invalid choice. Please select again.")
        advanced_medical_facility()
    alien_encounter()    

def alien_encounter():
    print(alien_encounter_story())
    while True:
        print("1. Communicate peacefully")
        print("2. Prepare defenses")
        choice = input("What do you do? (1 or 2): ")
        if choice == '1':
            print("The alien vessel shares technology that helps regenerate your energy.")
            health.gain_health(1)
            break
        elif choice == '2':
            print("Defensive actions lead to heightened tensions but avoid immediate danger.")
            break
        else:
            print("Invalid choice. Please select again.")
    resource_dilemma()

def resource_dilemma():
    print(resource_dilemma_story())
    while True:
        print("1. Ration supplies strictly")
        print("2. Keep current consumption")
        choice = input("How will you manage resources? (1 or 2): ")
        if choice == '1':
            print("Strict rationing helps conserve supplies but lowers morale.")
            break
        elif choice == '2':
            print("Resources run low, endangering the mission's final stages.")
            health.reduce_health(1)
            break
        else:
            print("Invalid choice. Please select again.")
    unexpected_visitor()

def unexpected_visitor():
    print(unexpected_visitor_story())
    while True:
        print("1. Attempt to help the adrift vessel")
        print("2. Preserve resources and ignore the signal")
        print("3. Contact your command for instructions")

        choice = input("How do you respond? (1, 2, or 3): ")
        if choice == '1':
            print("You decide to help, using up resources but gaining potential allies.")
            health.reduce_health(2)
            break
        elif choice == '2':
            print("You focus on your mission, ignoring the signal.")
            break
        elif choice == '3':
            print("You wait for further instructions, delaying your mission slightly.")
            break
        else:
            print("Invalid choice. Please select again.")
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