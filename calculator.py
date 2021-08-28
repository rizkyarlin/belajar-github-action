import math


def addition(a, b):
    return a


def divide(a, b):
    return a / b


def sum_three_numbers(a, b, c):
    return addition(addition(a, b), c)


def floor_after_addition():
    return math.floor(addition(1.7, 0.4)) # 2.1 -> 2
