import textwrap
import os
from utils import format_output
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


health = HealthManager()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("Press Enter to continue...")


def start_game():
    clear_screen()
    print(format_output(intro_story()))
    pause()
    initial_choice()


def initial_choice():
    clear_screen()
    while True:
        print(format_output(
            "What will you do next?\n"
            "1. Prepare the ship for launch\n"
            "2. Review mission details"
        ))
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            prepare_ship()
            break
        elif choice == '2':
            review_mission()
            break
        else:
            print("Invalid choice. Please select again.")
    pause()


def prepare_ship():
    clear_screen()
    print(format_output(prepare_ship_story()))
    health.reduce_health(1)
    print(f"Ship health: {health.get_health()}")
    pause()
    equipment_malfunction()


def review_mission():
    clear_screen()
    print(format_output(review_mission_story()))
    pause()
    equipment_malfunction()


def equipment_malfunction():
    clear_screen()
    print(format_output(equipment_malfunction_story()))
    while True:
        print(format_output(
            "1. Repair the life support system using spare parts\n"
            "2. Attempt a manual fix without using resources"
        ))
        choice = input("Choose your action (1 or 2): ")
        if choice == '1':
            print(format_output(
                "You've successfully repaired the system and conserved oxygen."
            ))
            health.gain_health(1)
            break
        elif choice == '2':
            print(format_output(
                "The manual fix failed, further straining the life support."
            ))
            health.reduce_health(1)
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    mid_journey_check()


def mid_journey_check():
    clear_screen()
    print(format_output(mid_journey_check_story()))
    while True:
        print(format_output(
            "1. Adjust shields to maximum\n"
            "2. Ignore and continue on current course\n"
            "3. Reroute to avoid the anomaly"
        ))
        choice = input("What's your command? (1, 2, or 3): ")
        if choice == '1':
            print(format_output(
                "Shields enhanced, energy consumption increases but you're "
                "safer."
            ))
            health.reduce_health(1)
            break
        elif choice == '2':
            print(format_output(
                "You take a risky gamble hoping the sensors are "
                "overreacting."
            ))
            break
        elif choice == '3':
            print(format_output(
                "Course adjusted, this will add time but you avoid potential "
                "hazards."
            ))
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    critical_meltdown()


def critical_meltdown():
    clear_screen()
    print(format_output(critical_meltdown_story()))
    print(format_output("1. Attempt to stabilize the reactor"))
    print(format_output("2. Abandon the reactor and evacuate"))
    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print(format_output(
            "You manage to stabilize the reactor, but the ship's systems are "
            "severely compromised."
        ))
        health.reduce_health(3)
        if health.get_health() <= 0:
            end_game()
            return
    elif choice == '2':
        print(format_output(
            "Evacuation is successful, but your ship suffers irreversible "
            "damage."
        ))
        health.reduce_health(2)
    else:
        print("Invalid choice. Please select again.")
        critical_meltdown()
    pause()
    advanced_medical_facility()


def advanced_medical_facility():
    clear_screen()
    print(format_output(advanced_medical_facility_story()))
    print(format_output("1. Integrate the health systems with your ship"))
    print(format_output("2. Leave the facility and continue the mission"))
    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print(format_output(
            "The integration is successful. Your ship's maximum health is "
            "increased and current health is fully restored."
        ))
        health.max_health += 2
    elif choice == '2':
        print(format_output(
            "You continue the mission without any enhancements."
        ))
    else:
        print("Invalid choice. Please select again.")
        advanced_medical_facility()
    pause()
    alien_encounter()


def alien_encounter():
    clear_screen()
    print(format_output(alien_encounter_story()))
    while True:
        print(format_output(
            "1. Communicate peacefully\n"
            "2. Prepare defenses"
        ))
        choice = input("What do you do? (1 or 2): ")
        if choice == '1':
            print(format_output(
                "The alien vessel shares technology that helps "
                "regenerate your energy."
            ))
            health.gain_health(1)
            break
        elif choice == '2':
            print(format_output(
                "Defensive actions lead to heightened tensions but avoid "
                "immediate danger."
            ))
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    resource_dilemma()


def resource_dilemma():
    clear_screen()
    print(format_output(resource_dilemma_story()))
    while True:
        print(format_output(
            "1. Ration supplies strictly\n"
            "2. Keep current consumption"
        ))
        choice = input("How will you manage resources? (1 or 2): ")
        if choice == '1':
            print(format_output(
                "Strict rationing helps conserve supplies but lowers morale."
            ))
            break
        elif choice == '2':
            print(format_output(
                "Resources run low, endangering the mission's final stages."
            ))
            health.reduce_health(1)
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    unexpected_visitor()


def unexpected_visitor():
    clear_screen()
    print(format_output(unexpected_visitor_story()))
    while True:
        print(format_output(
            "1. Attempt to help the adrift vessel\n"
            "2. Preserve resources and ignore the signal\n"
            "3. Contact your command for instructions"
        ))
        choice = input("How do you respond? (1, 2, or 3): ")
        if choice == '1':
            print(format_output(
                "You decide to help, using up resources but gaining potential "
                "allies."
            ))
            health.reduce_health(2)
            break
        elif choice == '2':
            print(format_output(
                "You focus on your mission, ignoring the signal."
            ))
            break
        elif choice == '3':
            print(format_output(
                "You wait for further instructions, delaying your mission "
                "slightly."
            ))
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    final_challenge()


def final_challenge():
    clear_screen()
    print(format_output(final_challenge_story()))
    if health.get_health() > 2:
        print(format_output(
            "You navigate the asteroid field successfully and your mission "
            "continues on course."
        ))
    else:
        print(format_output(
            "Your ship takes significant damage navigating through the "
            "asteroid field. Mission compromised."
        ))
    end_game()


def end_game():
    clear_screen()
    if health.get_health() > 3:
        print(format_output(
            "Congratulations! You've successfully launched the mission with "
            "your ship in good condition."
        ))
    elif health.get_health() > 0:
        print(format_output(
            "You barely manage to get your mission underway. It's going to be "
            "a challenging journey!"
        ))
    else:
        print(format_output(
            "Unfortunately, the ship is too damaged to continue. "
            "Mission failed."
        ))
    pause()


if __name__ == "__main__":
    start_game()