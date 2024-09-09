class HealthManager:
    def __init__(self, initial_health=5):
        self.health = initial_health
        self.max_health = initial_health

    def reduce_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("Your ship is too damaged to continue. Game Over.")
            exit()

    def gain_health(self, amount): # Increase health but not beyond the maximum health limit
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Health increased! Current health: {self.health}")

    def get_health(self):
        return self.health

    def instant_death(self):
        print("Critical failure! Your ship has been destroyed.")
        exit()

    def increase_max_health(self, new_max):
        self.max_health = new_max
        self.health = new_max
        print(f"Max health increased to {self.max_health}. Health fully restored.")