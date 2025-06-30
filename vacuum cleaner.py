class VacuumCleaner:
    def __init__(self):
        self.position = (0, 0)
        self.cleaned_positions = set()

    def move(self, direction):
        if direction == "up":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "down":
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "left":
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "right":
            self.position = (self.position[0] + 1, self.position[1])
        else:
            print("Invalid direction!")

    def clean(self):
        self.cleaned_positions.add(self.position)

    def status(self):
        return {
            "current_position": self.position,
            "cleaned_positions": self.cleaned_positions
        }

# Example usage
vacuum = VacuumCleaner()
vacuum.move("up")
vacuum.clean()
vacuum.move("right")
vacuum.clean()
print(vacuum.status())
