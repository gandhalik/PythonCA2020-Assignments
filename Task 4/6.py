# Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

a = "Consultadd Training"
b = a.split(" ")


def stringReverse(x):
    string = "".join(reversed(x))
    yield string


# reverse = stringReverse()
e = " "
for i in b:
    c = stringReverse(i)
    d = next(c)
    e = ''.join(d)
    print(e, end=" ")
