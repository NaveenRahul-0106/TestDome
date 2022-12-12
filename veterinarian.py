from collections import deque

class Veterinarian:
    def __init__(self):
        self.stack = deque()
    def accept(self, petName):
        self.stack.append(petName)

    def heal(self):
        return self.stack.popleft()

if __name__ == "__main__":
    veterinarian = Veterinarian()
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal()) # Should print: Barley
    print(veterinarian.heal()) # Should print: Mittens