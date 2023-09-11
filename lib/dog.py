#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name="Lucas", breed="Corgi"):
        if self.is_valid_name(name):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

        if self.is_valid_breed(breed):
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    def is_valid_name(self, name):
        return isinstance(name, str) and 1 <= len(name) <= 25

    def is_valid_breed(self, breed):
        return breed in APPROVED_BREEDS


# class Dog:
#     def __init__(self, name="Lucas", breed="Corgi"):
#         if isinstance(name, str) and 1 <= len(name) <= 25:
#             self.name = name
#         else:
#             print("Name must be string between 1 and 25 characters.")

#         if breed in APPROVED_BREEDS:
#             self.breed = breed
#         else:
#             print("Breed must be in list of approved breeds.")
