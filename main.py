"""
Case_3
Developers: Kabaev A., Anufrienko K., Lankevich S.
"""

from ru_local import *
import turtle


# TODO
def ice_frac_1(size, order):
    if order == 0:
        return turtle.forward(size)
    ice_frac_1(size / 3, order - 1)
    turtle.left(60)
    ice_frac_1(size / 3, order - 1)
    turtle.right(120)
    ice_frac_1(size / 3, order - 1)
    turtle.left(60)
    ice_frac_1(size / 3, order - 1)


def snowflake_1(size, order):
    for _ in range(6):
        ice_frac_1(size, order)
        turtle.right(120)
        ice_frac_1(size, order)
        turtle.right(120)
        ice_frac_1(size, order)
        turtle.right(180)
        ice_frac_1(size, order)
        turtle.left(120)
        ice_frac_1(size, order)
        turtle.left(120)
        ice_frac_1(size, order)
        turtle.right(180)
        ice_frac_1(size, order)
        turtle.right(60)

        
# TODO
def square(size, order):
    if not order:
        return
    turtle.up()
    turtle.forward(size / 4)
    turtle.down()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.right(10)
    return square(0.8 * size, order - 1)


def tree(size, order):
    if order == 0:
        return
    turtle.forward(size)
    turtle.right(30)
    tree(0.6 * size, order - 1)
    turtle.left(60)
    tree(0.6 * size, order - 1)
    turtle.right(30)
    turtle.backward(size)


def ice_frac_2(size, order):
    if order == 0:
        return turtle.forward(size)
    ice_frac_2(size / 2, order - 1)
    turtle.left(135)
    ice_frac_2(size / 3, order - 1)
    turtle.right(180)
    ice_frac_2(size / 3, order - 1)
    turtle.left(90)
    ice_frac_2(size / 3, order - 1)
    turtle.right(180)
    ice_frac_2(size / 3, order - 1)
    turtle.left(135)
    ice_frac_2(size / 2, order - 1)


def snowflake_2(size, order):
    for _ in range(6):
        ice_frac_2(size, order)
        turtle.right(120)
        ice_frac_2(size, order)
        turtle.right(120)
        ice_frac_2(size, order)
        turtle.right(180)
        ice_frac_2(size, order)
        turtle.left(120)
        ice_frac_2(size, order)
        turtle.left(120)
        ice_frac_2(size, order)
        turtle.right(180)
        ice_frac_2(size, order)
        turtle.right(60)


def ice_frac_3(size, order):
    if order == 0:
        return turtle.forward(size)
    ice_frac_3(size / 2, order - 1)
    turtle.left(90)
    ice_frac_3(size / 3, order - 1)
    turtle.right(180)
    ice_frac_3(size / 3, order - 1)
    turtle.left(90)
    ice_frac_3(size / 2, order - 1)


def snowflake_3(size, order):
    for _ in range(6):
        ice_frac_3(size, order)
        turtle.right(120)
        ice_frac_3(size, order)
        turtle.right(120)
        ice_frac_3(size, order)
        turtle.right(180)
        ice_frac_3(size, order)
        turtle.left(120)
        ice_frac_3(size, order)
        turtle.left(120)
        ice_frac_3(size, order)
        turtle.right(180)
        ice_frac_3(size, order)
        turtle.right(60)


def levi(size, order):
    if order == 0:
        return turtle.forward(size)
    turtle.left(45)
    levi(size * 1 / 2 ** (1 / 2), order - 1)
    turtle.right(90)
    levi(size * 1 / 2 ** (1 / 2), order - 1)
    turtle.left(45)


def dragon(size, order):
    if order == 0:
        return turtle.forward(size)
    turtle.right(45)
    dragon(size * 1 / 2 ** (1 / 2), order - 1)
    turtle.left(90)
    turtle.up()
    turtle.forward(size * 1 / 2 ** (1 / 2))
    turtle.down()
    turtle.left(180)
    dragon(size * 1 / 2 ** (1 / 2), order - 1)
    turtle.left(180)
    turtle.up()
    turtle.forward(size * 1 / 2 ** (1 / 2))
    turtle.down()
    turtle.right(45)

