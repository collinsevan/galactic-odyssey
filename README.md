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

### PEP 8 Testing

To ensure that all Python scripts in this project adhere to the PEP 8 style guide, we performed PEP 8 compliance testing using the **Code Institute Python Linter**, available at [PEP8CI](https://pep8ci.herokuapp.com/#). PEP 8 is the official style guide for Python, and adhering to it helps maintain clean, readable, and consistent code across the project.

The following scripts were tested for PEP 8 compliance:

- **game_logicval.py**
  ![game_logicval PEP 8 Compliance](assets/game_logicval.png)

- **Healthmanagerval.py**
  ![Healthmanagerval PEP 8 Compliance](assets/Healthmanagerval.png)

- **runpyval.py**
  ![runpyval PEP 8 Compliance](assets/runpyval.png)

- **storyval.py**
  ![storyval PEP 8 Compliance](assets/storyval.png)

- **resourcesval.py**
  ![resourcesval PEP 8 Compliance](assets/resourcesval.png)

- **utilsval.py**
  ![utilsval PEP 8 Compliance](assets/utilsval.png)

Each of these files was uploaded to the [PEP8CI linter](https://pep8ci.herokuapp.com/#), and the linter's output was reviewed to check for any PEP 8 violations. The linter checks for various coding standards, such as proper indentation, line length, spacing, naming conventions, and more, ensuring that the code follows best practices.

#### Results of PEP 8 Testing

After running all the files through the Code Institute Python Linter, the results were as follows:

- **No PEP 8 Errors or Warnings**: All the files listed above were found to be fully compliant with the PEP 8 guidelines. The linter did not report any errors or warnings, indicating that the code is clean, readable, and follows the standard Python coding style.

#### How to Test PEP 8 Compliance

If you wish to verify PEP 8 compliance for these files or any other files, you can follow these steps:

1. Visit the [PEP8CI linter](https://pep8ci.herokuapp.com/#) website.
2. Upload the Python file(s) you want to test.
3. Review the linter output for any PEP 8 compliance issues.

By ensuring PEP 8 compliance, we maintain a high standard of code quality and readability across the project.


### Lighthouse

Lighthouse is an open-source, automated tool used to improve the quality of web pages. It provides audits for performance, accessibility, best practices, SEO, and Progressive Web Apps (PWAs). To ensure that our project meets high standards across these categories, we used Lighthouse to run a series of tests on our application.

Below is the Lighthouse audit result for our project:

![Lighthouse Audit Results](assets/lighthouse.png)

### Explanation of Lighthouse Results

- **Performance**: This metric assesses how quickly the application loads and becomes interactive. Our project achieved a strong performance score, indicating efficient resource use, fast loading times, and minimal render-blocking resources.
  
- **Accessibility**: This score represents how accessible the application is to all users, including those with disabilities. A high score was achieved, reflecting our use of semantic HTML, proper color contrast, alt attributes for images, and keyboard navigation support.

- **Best Practices**: This metric evaluates whether the site adheres to web development best practices, such as using HTTPS, avoiding deprecated APIs, and ensuring that images are optimized. Our project scored highly, showcasing our commitment to modern development standards.

- **SEO**: The SEO score assesses how well-optimized the application is for search engines. A high score indicates that the site follows best practices for content discoverability, such as proper use of meta tags, heading structures, and descriptive link text.

- **Progressive Web App (PWA)**: If applicable, the PWA score evaluates how well the application is set up to work as a Progressive Web App. A high score here reflects our project’s readiness to offer a reliable, installable experience similar to native applications.

### How to Perform a Lighthouse Audit

To perform a Lighthouse audit yourself, follow these steps:

1. Open the project in **Google Chrome**.
2. Right-click on the page and select **Inspect** to open Chrome DevTools.
3. Go to the **Lighthouse** tab in the DevTools panel.
4. Choose the desired categories to audit (Performance, Accessibility, Best Practices, SEO, PWA) and click **Generate Report**.
5. Review the results and adjust the application as needed to improve the scores.

Regular Lighthouse audits help maintain high standards in performance, accessibility, and other key areas, ensuring an excellent user experience across different devices and network conditions.


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