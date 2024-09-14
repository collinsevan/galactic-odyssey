class HealthManager:
    def __init__(self, initial_health=5):
        """
        Initialize the HealthManager with a specified initial health.
        :param initial_health: The starting health value (default is 5).
        """
        self.health = initial_health
        self.max_health = initial_health

    def reduce_health(self, amount):
        """
        Reduce health by a given amount.
        Exit the game if health drops to zero or below.
        :param amount: The amount to reduce health by.
        """
        self.health -= amount
        if self.health <= 0:
            print("Your ship is too damaged to continue. Game Over.")
            exit()

    def gain_health(self, amount):
        """
        Increase health by a given amount.
        Ensure health does not exceed max_health.
        :param amount: The amount to increase health by.
        """
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Health increased! Current health: {self.health}")

    def get_health(self):
        """
        Get the current health value.
        :return: The current health value.
        """
        return self.health

    def set_max_health(self, amount):
        """
        Set a new maximum health value.
        Adjust current health if it exceeds the new max_health.
        :param amount: The new maximum health value.
        """
        self.max_health = amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Max health increased! New max health: {self.max_health}")

    def restore_health(self):
        """
        Restore health to the maximum value.
        """
        self.health = self.max_health  # Restore health to max health
        print(f"Health restored to full! Current health: {self.health}")
