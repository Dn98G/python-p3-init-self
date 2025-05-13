#!/usr/bin/env python3

class Dog:
    def __init__ (self, name,breed="Mutt"):
        self.name = name
        self.breed = breed
snoopy = Dog("Snoopy", "Beagle")
snoopy2 = Dog("Snoopy2")
print(snoopy2.breed)