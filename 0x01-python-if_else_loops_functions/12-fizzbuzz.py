#usr/bin/python3
# Author - Thobile
"""Print the number fromm 1 to 100 seperated by a space"""
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{}".format(number), end=" ")
