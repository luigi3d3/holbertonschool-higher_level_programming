#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#abs es para para generar numeros absolutos 
last_digit = abs(number % 10)

if number > 0:
    print(f"Last digit of {number} is {last_digit}", end=" ")
else:
    print(f"Last digit of {number} is -{abs(last_digit)}", end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print(f"and us less than 6 and not 0")
