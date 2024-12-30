#!/usr/bin/env python3

class Dog:
    # Instance method definition
    def bark(self):
        # Fixing the case to match expected output
        print("Woof!")

    def sit(self):
        # Ensuring the output matches expected format
        print("The dog is sitting.")

# Creating Dog instances and calling their methods
fido = Dog()
fido.bark()

snoopy = Dog()
snoopy.bark()

doogy = Dog()
doogy.sit()
