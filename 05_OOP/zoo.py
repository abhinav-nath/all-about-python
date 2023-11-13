class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  # To be overridden by subclasses


class Lion(Animal):
    def make_sound(self):
        return "Roar!"


class Elephant(Animal):
    def make_sound(self):
        return "Trumpet!"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name} ({animal.species}): {animal.make_sound()}")


# Usage
if __name__ == "__main__":
    # Create animals
    lion = Lion(name="Simba", species="Lion")
    elephant = Elephant(name="Dumbo", species="Elephant")

    # Create a zoo
    my_zoo = Zoo()

    # Add animals to the zoo
    my_zoo.add_animal(lion)
    my_zoo.add_animal(elephant)

    # Display the animals in the zoo
    my_zoo.display_animals()
