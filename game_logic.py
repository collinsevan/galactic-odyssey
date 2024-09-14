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
    final_challenge_story,
    emergency_repair_story,
    resource_discovery_story,
    space_station_rescue_story,
    unexpected_upgrade_story
)
from health_manager import HealthManager

health = HealthManager()
resources = 1  # Initialize resources with 1


def clear_screen():
    """
    Clears the terminal screen for better readability.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """
    Pauses the execution until the user presses Enter.
    """
    input("Press Enter to continue...")


def start_game():
    """
    Starts the game by displaying the introductory story and
    proceeding to the initial choice.
    """
    clear_screen()
    print(format_output(intro_story()))
    pause()
    initial_choice()


def initial_choice():
    """
    Prompts the user to make an initial choice to either prepare
    the ship or review mission details.
    """
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
    """
    Handles the preparation of the ship for launch and proceeds
    to the equipment malfunction scenario.
    """
    clear_screen()
    print(format_output(prepare_ship_story()))
    health.reduce_health(1)
    print(f"Ship health: {health.get_health()}")
    print(f"Resources: {resources}")  # Show resources
    pause()
    equipment_malfunction()


def review_mission():
    """
    Displays the mission review details and proceeds to the
    equipment malfunction scenario.
    """
    clear_screen()
    print(format_output(review_mission_story()))
    pause()
    equipment_malfunction()


def equipment_malfunction():
    """
    Presents the equipment malfunction scenario, allowing the user
    to choose between repairing the system with resources or
    attempting a manual fix.
    """
    global resources  # Declare global variable usage
    clear_screen()
    print(format_output(equipment_malfunction_story()))
    while True:
        print(format_output(
            "1. Repair the life support system using spare parts\n"
            "2. Attempt a manual fix without using resources"
        ))
        choice = input("Choose your action (1 or 2): ")
        if choice == '1':
            if resources > 0:
                print(format_output(
                    "You've successfully repaired the system and "
                    "conserved oxygen."
                ))
                health.gain_health(1)
                resources -= 1  # Use a resource
                print(f"Resources: {resources}")  # Show resources
            else:
                print("Not enough resources to repair the system.")
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
    """
    Allows the user to make decisions about the ship's shields
    and course in response to a mid-journey anomaly.
    """
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
    """
    Deals with a critical reactor meltdown scenario, giving the user
    options to stabilize the reactor or evacuate.
    """
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
    """
    Provides options to integrate with or leave an advanced medical
    facility, affecting the ship's health.
    """
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
        health.restore_health()
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
    """
    Allows the user to interact with an alien vessel, choosing between
    peaceful communication or preparing defenses.
    """
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
    """
    Presents a resource management dilemma, where the user decides
    between strict rationing or maintaining current consumption.
    """
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
    """
    Deals with an unexpected visitor scenario, giving options to
    help the visitor, ignore them, or wait for command instructions.
    """
    global resources  # Declare global variable usage
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
            if resources >= 2:
                print(format_output(
                    "You decide to help, using up resources but gaining\n"
                    "potential allies."
                ))
                resources -= 2  # Use resources
                print(f"Resources: {resources}")  # Show resources
            else:
                print("Not enough resources to help the vessel.")
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
    emergency_repair()


def emergency_repair():
    """
    Handles an emergency repair situation, allowing the user to
    choose between using resources for a quick fix or attempting
    a manual repair.
    """
    global resources  # Declare global variable usage
    clear_screen()
    print(format_output(emergency_repair_story()))
    while True:
        print(format_output(
            "1. Use resources for a quick repair\n"
            "2. Attempt a manual repair"
        ))
        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            if resources > 0:
                print(format_output(
                    "You successfully repair the engine using resources."
                ))
                resources -= 1  # Use a resource
                health.gain_health(1)
                print(f"Resources: {resources}")  # Show resources
            else:
                print("Not enough resources for the quick repair.")
            break
        elif choice == '2':
            print(format_output(
                "The manual repair fails, causing additional damage."
            ))
            health.reduce_health(2)
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    resource_discovery()


def resource_discovery():
    """
    Deals with discovering new resources, allowing the user to
    either integrate them into the ship or save them for emergencies.
    """
    global resources  # Declare global variable usage
    clear_screen()
    print(format_output(resource_discovery_story()))
    while True:
        print(format_output(
            "1. Use the new resources to improve the ship\n"
            "2. Save the resources for emergencies"
        ))
        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            print(format_output(
                "You integrate the new resources into the ship, boosting its "
                "performance."
            ))
            resources += 2  # Gain resources
            print(f"Resources: {resources}")  # Show resources
            break
        elif choice == '2':
            print(format_output(
                "You decide to save the resources for potential emergencies."
            ))
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    space_station_rescue()


def space_station_rescue():
    """
    Handles the decision to rescue a space station crew or continue
    to Titan V without intervention.
    """
    clear_screen()
    print(format_output(space_station_rescue_story()))
    while True:
        print(format_output(
            "1. Rescue the crew and provide supplies\n"
            "2. Continue to Titan V without intervention"
        ))
        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            if resources >= 3:
                print(format_output(
                    "You successfully rescue the crew and provide essential "
                    "supplies."
                ))
                resources -= 3  # Use resources
                health.gain_health(2)
                print(f"Resources: {resources}")  # Show resources
            else:
                print("Not enough resources to complete the rescue.")
            break
        elif choice == '2':
            print(format_output(
                "You continue to Titan V without aiding the station."
            ))
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    unexpected_upgrade()


def unexpected_upgrade():
    """
    Handles the situation of receiving an unexpected upgrade, allowing
    the user to either apply the upgrade immediately or save it for
    later use.
    """
    clear_screen()
    print(format_output(unexpected_upgrade_story()))
    while True:
        print(format_output(
            "1. Apply the upgrade to improve ship systems\n"
            "2. Save the upgrade for later use"
        ))
        choice = input("What will you do? (1 or 2): ")
        if choice == '1':
            print(format_output(
                "The upgrade enhances your ship's performance."
            ))
            health.gain_health(1)
            break
        elif choice == '2':
            print(format_output(
                "You choose to save the upgrade for later use."
            ))
            break
        else:
            print("Invalid choice. Please select again.")
    pause()
    final_challenge()


def final_challenge():
    """
    Presents the final challenge of navigating through an asteroid field
    or finding an alternate route.
    """
    clear_screen()
    print(format_output(final_challenge_story()))
    print(format_output("1. Navigate through the asteroid field"))
    print(format_output("2. Attempt to find an alternate route"))
    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        print(format_output(
            "You navigate through the asteroid field with skill, but it "
            "takes a toll on the ship."
        ))
        health.reduce_health(2)
    elif choice == '2':
        print(format_output(
            "You find an alternate route, avoiding immediate danger but "
            "adding time to your journey."
        ))
    else:
        print("Invalid choice. Please select again.")
        final_challenge()
    pause()
    end_game()


def end_game():
    """
    Ends the game and displays the final message.
    """
    clear_screen()
    print(format_output(
        "Congratulations! You've completed your mission to Titan V.\n"
        "Your journey had many challenges, but you navigated them all.\n"
        "Thank you for playing!"
    ))
    exit()