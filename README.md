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

## How to Deploy Your App on Heroku

1. **Start a New App**
   - In your Heroku dashboard, click on "New" and select "Create new app".
   - Provide a unique name for your application.
   - Choose the appropriate region for your deployment.
   - Click "Create app" to initialize your new app.

2. **Configure Environment Variables**
   - Go to the "Settings" tab of your app.
   - Find the "Config Vars" section and click "Reveal Config Vars".
   - Add the necessary configuration variables. For instance, set `PORT` as the key and `8000` as the value.
   - Click "Add" to save your settings.

3. **Set Up Buildpacks**
   - In the "Settings" tab, locate the "Buildpacks" section and click "Add buildpack".
   - Add the "python" buildpack first, then click "Save changes".
   - Add the "node.js" buildpack next and click "Save changes" again.

4. **Deploy Your Application**
   - Navigate to the "Deploy" tab.
   - Choose "GitHub" as your deployment method and connect your GitHub account if needed.
   - Search for your repository and click "Connect" to link it with Heroku.
   - In the "Deploy" section, you can choose between:
     - **Automatic Deploys**: Enable this option to automatically deploy your app whenever you push updates to GitHub.
     - **Manual Deploy**: Select the branch you want to deploy and click "Deploy Branch" to start the deployment process manually.

5. **Access Your App**
   - Monitor the build and deployment progress on the Heroku dashboard.
   - Once the deployment is complete, you can view your app by clicking "Open app" at the top of the page.

### Steps to Clone Site

1. **Clone the Repository**: To clone the repository to your local machine, use the Git clone command. Replace `REPOSITORY_URL` with the URL of the repository:
    ```bash
    git clone REPOSITORY_URL
    ```

2. **Navigate to the Project Directory**: Change to the directory where the project was cloned:
    ```bash
    cd PROJECT_DIRECTORY
    ```

3. **Set Up Your Environment**: If the project requires any environment variables or dependencies, set them up according to the project's documentation. For a Python project, you might need to install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application Locally**: Start the application locally to ensure it works as expected:
    ```bash
    python run.py
    ```

5. **Update Remote Settings**: If you plan to push changes back to the original repository, ensure your Git remote settings are correct:
    ```bash
    git remote -v
    ```

6. **Push Changes**: To push any local changes to the repository, commit them first and then push:
    ```bash
    git add .
    git commit -m "Your message"
    git push origin master
    ```

## Credits

## Acknowledgements