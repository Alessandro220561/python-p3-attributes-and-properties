#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


# class Person:
#     def __init__(self, name="Alessandro", job="Legal"):
#         if self.is_valid_name(name):
#             self.name = name.title()
#         else:
#             print("Name must be string between 1 and 25 characters.")

#         if self.is_valid_job(job):
#             self.job = job
#         else:
#             print("Job must be in list of approved jobs.")

#     def is_valid_name(self, name):
#         valid_name = str(isinstance(name, str) and 1 >=
#                          len(name) <= 25)
#         return valid_name

#     def is_valid_job(self, job):
#         return job in APPROVED_JOBS


class Person:
    def __init__(self, name="Jon", job="Legal"):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")
