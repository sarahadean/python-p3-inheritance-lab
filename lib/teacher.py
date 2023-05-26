#!/usr/bin/env python

from user import User

import random

# knowledge = [
#     "str is a data type in Python",
#     "programming is hard, but it's worth it",
#     "JavaScript async web request",
#     "Python function call definition",
#     "object-oriented teacher instance",
#     "programming computers hacking learning terminal",
#     "pipenv install pipenv shell",
#     "pytest -x flag to fail fast",
# ]

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

    def teach(self):
    #    print(self.knowledge)
       random_fact = random.randint(0, len(self.knowledge)-1)
       return self.knowledge[random_fact]

mrs_smith = Teacher("Mary", "Smith")
# print(mrs_smith.knowledge)
#successful

# print(mrs_smith.teach())
#successfully printed random thing from knowledge list

