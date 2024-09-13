# Galactic Odyssey

## Table of Contents

- [User Experience](#user-experience)
- [Features](#features)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience

### User Story
As a user,
- I would like to understand how to interact with the game.
- I would like to be able to make decisions within the game that determine wether I win or fail.
- I would like the options I have to be clearly presented to me.
- I would like to be able to replay the game when I reach an ending.

## Features

### Title Screen
- The game starts with a welcome message.
- Users press Enter to start the adventure or 'h' for help.

### Help Menu
- Provides an overview of game mechanics, including managing ship health and resources.

### Game Flow
- **Intro Story**: Introduction to the mission and preparation for launch.
- **Prepare the Ship**: Address system alerts and prepare the ship for departure.
- **Review Mission**: Review mission parameters and ensure readiness.
- **Equipment Malfunction**: Handle critical equipment failures.
- **Mid-Journey Check**: Respond to space weather conditions.
- **Critical Meltdown**: Decide how to handle a reactor meltdown.
- **Advanced Medical Facility**: Choose whether to integrate advanced medical technology.
- **Alien Encounter**: Choose how to interact with an alien spacecraft.
- **Resource Dilemma**: Manage dwindling resources.
- **Unexpected Visitor**: Decide how to respond to an adrift vessel.
- **Final Challenge**: Navigate through an asteroid field to complete the mission.

### Making Decisions
- Players are prompted to make choices that influence the mission’s outcome.

### Game End
- The game concludes with a summary based on ship health and performance throughout the journey.

## User Interaction

The game is designed to be text-based, guiding the player through various scenarios with choices that impact the game's outcome. Interaction is primarily through input commands that determine the direction of the story. Players make decisions by entering numeric choices corresponding to the available options. The game progresses based on these choices, affecting the player's health, resources, and mission success.

Key interactions include:

- **Initial Choices**: Players start by preparing the ship or reviewing the mission details.
- **Resource Management**: Players manage limited resources to navigate through various challenges.
- **Health Monitoring**: The player's health is influenced by their choices and can affect the game outcome.
- **Story Progression**: Players encounter different scenarios (e.g., equipment malfunction, alien encounters) and make decisions that impact their journey.

## End Screen

The end screen is displayed when the player completes their mission or their health reaches zero. It provides a summary of the player's journey, highlights key achievements or failures, and thanks the player for participating.

The end screen includes:

- **Mission Outcome**: A summary of whether the mission to Titan V was successfully completed or if it ended in failure.
- **Health and Resources Summary**: A recap of the player's final health status and resources.
- **Acknowledgements**: A thank you note to the player for their engagement with the game.
- **Exit Option**: An option to exit the game.

## Future Expansion

Future updates to the game could include:

- **Additional Story Scenarios**: Introducing new scenarios to expand the narrative and provide more variety in gameplay.
- **Enhanced Graphics**: Incorporating graphical elements or animations to complement the text-based storytelling.
- **Sound Effects and Music**: Adding audio elements to enrich the immersive experience.
- **Expanded Choices and Consequences**: Implementing more complex decision-making processes and their impact on the story.
- **Multiplayer Mode**: Exploring options for cooperative or competitive gameplay with other players.

## Design

### Story

The game’s story is central to its design, revolving around the player’s journey as the captain of the spaceship *Starfire*. The narrative unfolds through a series of interconnected scenarios where the player’s choices influence the outcome. The story includes:

- **Introduction**: Sets the stage for the mission and establishes the setting.
- **Challenges**: Various scenarios, such as equipment malfunctions and alien encounters, where players make critical decisions.
- **Resolution**: Concludes with the final challenge and an end screen summarizing the mission's outcome.

### Graphics

The current version of the game is text-based, focusing on narrative and player choice rather than visual elements. Future versions may include:

- **Character and Environment Graphics**: Illustrations of the spaceship, alien encounters, and other elements of the game.
- **User Interface Enhancements**: Improved layouts and visuals for a more engaging experience.

## Technologies Used

- **Python**: The primary programming language used for game development.
- **Textwrap Module**: Utilized for formatting text output to ensure readability and consistency.
- **OS Module**: Employed for clearing the screen and managing system-specific operations.
- **Utils Module**: Contains utility functions such as `format_output` to standardize text formatting across the game.
- **Health Management**: Implemented through a `HealthManager` class to handle player health and related operations.

## Testing

### PEP8 online check

### Lighthouse

### Browser Compatibility

### Testing Functionality

### Testing User Stories

## Deployment

### Steps to deploy site using Heroku

### Steps to clone site

## Credits

## Acknowledgements