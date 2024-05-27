import math
import cmath


def solve(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.

    TypeError: если аргументы не являются числами.
    ValueError: если коэффициент a равен нулю.

    :param a: (float или int): коэффициент уравнения.
    :param b: (float или int): коэффициент уравнения.
    :param c: (float или int): коэффициент уравнения.
    :return: list: список корней уравнения. Пустой список, если действительных корней нет.
    """
    if not all(isinstance(i, (float, int)) for i in [a, b, c]):
        raise TypeError('Все аргументы должны быть числами')

    if abs(a) < math.ulp(1.0):
        raise ValueError('Коэффициент a не может быть нулем')

    discr = b ** 2 - 4 * a * c
    if discr > math.ulp(1.0):
        root1 = (-b + cmath.sqrt(discr)) / (2 * a)
        root2 = (-b - cmath.sqrt(discr)) / (2 * a)
        return [root1, root2]
    elif abs(discr) <= math.ulp(1.0):
        root = -b / (2 * a)
        return [root]
    else:
        return []


def test_1():
    """
    проверяет, что для уравнения x2+1=0
    корней нет. Ожидается, что функция solve вернет пустой список.
    """
    assert len(solve(1, 0, 1)) == 0


def test_2():
    """
    проверяет, что для уравнения x2−1=0
    есть два корня кратности 1 (x1=1, x2=-1).
    Ожидается, что функция solve вернет список с двумя корнями: [1, -1].
    """
    assert len(solve(1, 0, -1)) == 2
    assert solve(1, 0, -1) == [1, -1]


def test_3():
    """
    проверяет, что для уравнения x2+2x+1=0
    есть один корень кратности 2 (x1= x2 = -1).
    Ожидается, что функция solve вернет список с одним корнем: [-1].
    """
    assert len(solve(1, 2, 1)) == 1
    assert solve(1, 2, 1) == [-1]


def test_4():
    """
    проверяет, что коэффициент a не может быть равен 0.
    В этом случае solve должна выбросить исключение ValueError с сообщением ‘Коэффициент a не может быть нулем.
    """
    try:
        solve(0, 0, 0)
    except ValueError as e:
        assert str(e) == 'Коэффициент a не может быть нулем'


def test_5():
    """
    проверяет, что все аргументы функции solve должны быть числами.
    Если это не так, solve должна выбросить исключение TypeError с сообщением ‘Все аргументы должны быть числами
    """
    try:
        solve('x1', 'x2', 'x3')
    except TypeError as e:
        assert str(e) == 'Все аргументы должны быть числами'


def test_6():
    """
    проверяет случай, когда дискриминант отличен от нуля, но меньше заданного эпсилон.
    В этом случае ожидается, что функция solve вернет список с одним корнем
    """
    assert len(solve(1e-15, 1e-15, 1e-15)) == 1


def test_7():
    """
    проверяет, что функция solve выбрасывает исключение TypeError для каждого из значений:
    float('inf'), float('-inf') и float('nan').
    Эти значения не являются числами в обычном понимании, поэтому solve должна выбросить исключение,
    если они передаются в качестве аргументов.
    """
    for val in [float('inf'), float('-inf'), float('nan')]:
        try:
            solve(val, val, val)
        except TypeError as e:
            assert str(e) == 'Все аргументы должны быть числами'
