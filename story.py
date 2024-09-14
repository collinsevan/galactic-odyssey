import textwrap
from utils import format_output


def intro_story():
    return format_output(
        "You are the captain of the spaceship *Starfire*, "
        "assigned to deliver critical supplies to the colony "
        "on Titan V. Your journey through deep space will be "
        "fraught with danger. Stay sharp and make the right "
        "choices to complete your mission.", width=55
    )


def prepare_ship_story():
    return format_output(
        "As you begin preparations for launch, you notice a "
        "series of system alerts. The fuel line has a leak, "
        "and the navigation system needs recalibration. Quick "
        "decisions and precise actions are needed to avoid delays.", width=55
    )


def review_mission_story():
    return format_output(
        "You decide to review the mission parameters and "
        "double-check the cargo manifest. Everything must be "
        "accounted for, and no errors can be tolerated if the "
        "mission is to succeed. Your careful review ensures that "
        "all systems are operational.", width=55
    )


def equipment_malfunction_story():
    return format_output(
        "Just as you settle into the journey, a critical alert "
        "sounds. The life support system has malfunctioned, "
        "threatening the air supply. Immediate action is required "
        "to ensure the safety of everyone aboard.", width=55
    )


def mid_journey_check_story():
    return format_output(
        "Midway through your journey, the ship's sensors detect "
        "abnormal space weather conditions that could jeopardize "
        "your navigation systems. Your action here is crucial to "
        "maintain your course.", width=55
    )


def critical_meltdown_story():
    return format_output(
        "A critical reactor meltdown is imminent. Immediate action "
        "is required to stabilize the reactor or evacuate the ship. "
        "This decision could have serious consequences for your "
        "mission and crew.", width=55
    )


def advanced_medical_facility_story():
    return format_output(
        "You find an advanced medical facility in space. It offers "
        "technology to enhance your ship's health systems. How you "
        "use this opportunity will impact your mission.", width=55
    )


def alien_encounter_story():
    return format_output(
        "An unidentified alien spacecraft approaches. Their "
        "intentions are unclear, and you must decide how to respond "
        "without provoking a conflict or missing a potential ally.", width=55
    )


def resource_dilemma_story():
    return format_output(
        "Resources are running low due to earlier issues. Decide "
        "whether to ration supplies, affecting morale, or maintain "
        "current consumption, risking shortages later.", width=55
    )


def unexpected_visitor_story():
    return format_output(
        "As you approach Titan V, an unidentified distress signal "
        "is picked up from an adrift vessel. How you handle this "
        "could affect your resources and moral code.", width=55
    )


def emergency_repair_story():
    return format_output(
        "Critical malfunction in the ship's engine requires immediate "
        "attention. Decide whether to use resources for a quick fix or "
        "attempt a riskier manual repair.", width=55
    )


def resource_discovery_story():
    return format_output(
        "You find a cache of supplies guarded by alien technology. "
        "Decide whether to use resources to retrieve these supplies or "
        "avoid the risk and continue your mission.", width=55
    )


def space_station_rescue_story():
    return format_output(
        "A damaged space station with survivors needs assistance. "
        "You must decide if you will use resources to aid them or "
        "proceed with your mission, conserving your own resources.", width=55
    )


def unexpected_upgrade_story():
    return format_output(
        "An unknown alien device offers a potential upgrade to your ship. "
        "You need to decide whether to invest resources for the upgrade or "
        "continue without it, potentially risking mission success.", width=55
    )


def final_challenge_story():
    return format_output(
        "Approaching Titan V, you're alerted to an asteroid field "
        "in your path. Navigating it requires skill and nerve. This "
        "is the final test of your readiness for the mission.", width=55
    )
