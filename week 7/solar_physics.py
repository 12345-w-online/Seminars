from random import randint
import math
pi = math.pi


gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    global gravitational_constant, pi
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            pass
        else:
            r_2 = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2)
            F = (gravitational_constant * body.m * obj.m) / r_2
            # a это угол между вектором силы и горизонталью 
            a = math.atan(obj.y - body.y) / (obj.x - body.x)
            # cosinus a со знаком
            cos_a = math.cos(a if obj.x - body.x >0 else abs(a) + (pi / 2))
            sin_a = math.sin(a) if obj.x - body.x >0 else -1 * math.sin(a)

            body.Fx = body.Fx + F * cos_a
            body.Fy = body.Fy + F * -sin_a


def move_space_object(body, dt):
    
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    body.x = body.x + body.Vx * dt
    body.Vx = body.Vx + ax * dt

    ay = body.Fy / body.m
    # body.Vy =0
    body.y = body.y + body.Vy * dt
    body.Vy = body.Vy + ay * dt 
    print(ay, body.Vy)
    # body.Vy = 0 
    '''zhitь ( ͡ಥ ͜ʖ ͡ಥ)'''


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать
    координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
