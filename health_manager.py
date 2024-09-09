class HealthManager:
    def __init__(self, initial_health=5):
        self.health = initial_health
        self.max_health = initial_health  # Add this attribute to track max health

    def reduce_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("Your ship is too damaged to continue. Game Over.")
            exit()

    def gain_health(self, amount):
        self.health += amount
        if self.health > self.max_health:  # Ensure health does not exceed max_health
            self.health = self.max_health
        print(f"Health increased! Current health: {self.health}")

    def get_health(self):
        return self.health

    def set_max_health(self, amount):
        self.max_health = amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Max health increased! New max health: {self.max_health}")

    def restore_health(self):
        self.health = self.max_health  # Restore health to max health
        print(f"Health restored to full! Current health: {self.health}")