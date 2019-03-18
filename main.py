"""
Case_3
Developers: Kabaev A., Anufrienko K.
"""
import turtle


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


def branch(size, order):
    if order == 0:
        return
    turtle.forward(size / 2)
    turtle.left(45)
    branch(size / 4, order - 1)
    turtle.right(90)
    branch(size / 4, order - 1)
    turtle.left(45)
    branch(size / 2, order - 1)
    turtle.forward(size / 2)
    turtle.backward(size)


def mink_curve(size, order):
    if order == 0:
        return turtle.forward(size)
    mink_curve(size / 4, order - 1)
    turtle.left(90)
    mink_curve(size / 4, order - 1)
    turtle.right(90)
    mink_curve(size / 4, order - 1)
    turtle.right(90)
    mink_curve(size / 4, order - 1)
    mink_curve(size / 4, order - 1)
    turtle.left(90)
    mink_curve(size / 4, order - 1)
    turtle.left(90)
    mink_curve(size / 4, order - 1)
    turtle.right(90)
    mink_curve(size / 4, order - 1)


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


def main():
    text_input = 'Доступные рисунки: \n\ 
    убегающий квадрат(1), двоичное дерево(2), ветка(3), кривая Коха(4),\n\ 
    cнежинка Коха(5), кривая Минковского(6), "ледяной" фрактал № 1(7), кривая Леви(8), \n\
    дракон Хартера-Хейтуэя(9),  "ледяной" фрактал № 2(10), "ледяной" фрактал № 3(11), "ледяной" фрактал № 4(12) \n'
    _list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    chos = turtle.textinput("chos", text_input + 'Выберите рисунок: ')
    while chos not in _list:
        turtle.textinput("chos", text_input + 'Введите корректный номер: ')
    order = turtle.numinput('order', 'Введите глубину рекурсии:', 3)
    chos = int(chos)
    size = turtle.numinput('order', 'Введите размер:', 100)
    turtle.speed(9)
    if chos == 1:
        square(size, order)
    elif chos == 2:
        turtle.left(90)
        tree(size, order)
    elif chos == 3:
        turtle.left(90)
        branch(size, order)
    elif chos == 4:
        snowflake_1(size, order)
    elif chos == 5:
        snowflake_3(size, order)
    elif chos == 6:
        mink_curve(size, order)
    elif chos == 7:
        ice_frac_1(size, order)
    elif chos == 8:
        levi(size, order)
    elif chos == 9:
        dragon(size, order)
    elif chos == 10:
        ice_frac_2(size, order)
    elif chos == 11:
        ice_frac_3(size, order)
    elif chos == 12:
        snowflake_2(size, order)
    turtle.mainloop()


if __name__ == '__main__':
    main()
