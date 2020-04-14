# Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to
# use only higher order function.

# Not divisible by 3 and multiple of 7 for a given number
# Result function with N


def result(n):
    # iterate from 0 to n
    for num in range(n):

        if num % 3 != 0:
            x = num / 7
            if x % 5 == 0:
                print(str(num) + " ", end="")

        else:
            pass


# Driver code
if __name__ == "__main__":
    # input goes here
    n = 100

    # Calling function
    result(n)
