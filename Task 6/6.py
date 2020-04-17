class Person:

    def __init__(self, initial_age):
        self.age = initial_age if initial_age >= 0 else 0
        if initial_age < 0:
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.age += 1
        return self.age


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
