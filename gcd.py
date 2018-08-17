def gcd(a,b):
    """ Рекурсивный Алгоритм Евклида для двух значений a и b
        Находит их Наименьший Общий Делитель
    """
    return a if b ==0 else gcd(b, a % b)


def test_gcd():
    m = gcd(5,3)
    print("Testcase #1 - ","Ok" if m == 1 else "False")
    m = gcd(96, 27)
    print("Testcase #2 - ","Ok" if m == 3 else "False")
    m = gcd(34, 17)
    print("Testcase #3 - ","Ok" if m == 17 else "False")

test_gcd()
