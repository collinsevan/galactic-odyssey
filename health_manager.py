class HealthManager:
    def __init__(self, initial_health=5):
        self.health = initial_health

    def reduce_health(self, amount):
        # Reduce health
        self.health -= amount
        if self.health <= 0:
            print("Your ship is too damaged to continue. Game Over.")
            exit()

    def gain_health(self, amount):
        self.health += amount  # Increase health by the specified amount
        print(f"Health increased! Current health: {self.health}")

    def get_health(self):
        return self.health