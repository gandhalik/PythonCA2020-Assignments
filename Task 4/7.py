def our_decorator(func):
    def training(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)

    return training


def lecture(x):
    print("I am enjoying this class: " + str(x))


print('I am excited to join:')
lecture("Hi")

print("We are learning with:")
lecture = our_decorator(lecture)

print("We have our class at:")
lecture(8)
