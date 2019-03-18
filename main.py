"""
Case_3
Developers: Kabaev A., Anufrienko K., Lankevich S.
"""

from ru_local import *
import turtle


# TODO

# TODO

# TODO
def k(d, n):
    if not n:
        return
    turtle.up()
    turtle.forward(d/4)
    turtle.down()
    for _ in range(4):
        turtle.forward(d)
        turtle.right(90)
    turtle.right(10)
    return k(0.8 * d, n - 1)


def tree(d, n):
    if n == 0:
        return
    turtle.forward(d)
    turtle.right(30)
    tree(0.6 * d, n - 1)
    turtle.left(60)
    tree(0.6 * d, n - 1)
    turtle.right(30)
    turtle.backward(d)


def ice_frac_2(d, n):
    if n == 0:
        return turtle.forward(d)
    ice_frac_2(d, n - 1)
    turtle.left(135)
    ice_frac_2(d / 2, n - 1)
    turtle.right(180)
    ice_frac_2(d / 2, n - 1)
    turtle.left(90)
    ice_frac_2(d / 2, n - 1)
    turtle.right(180)
    ice_frac_2(d / 2, n - 1)
    turtle.left(135)
    ice_frac_2(d, n - 1)


def levi(d, n):
    if n == 0:
        return turtle.forward(d)
    turtle.left(45)
    levi(d * 1 / 2 ** (1 / 2), n - 1)
    turtle.right(90)
    levi(d * 1 / 2 ** (1 / 2), n - 1)
    turtle.left(45)


def dragon(d, n):
    if n == 0:
        return turtle.forward(d)
    turtle.right(45)
    dragon(d * 1 / 2 ** (1 / 2), n - 1)
    turtle.left(90)
    turtle.up()
    turtle.forward(d * 1 / 2 ** (1 / 2))
    turtle.down()
    turtle.left(180)
    dragon(d * 1 / 2 ** (1 / 2), n - 1)
    turtle.left(180)
    turtle.up()
    turtle.forward(d * 1 / 2 ** (1 / 2))
    turtle.down()
    turtle.right(45)

