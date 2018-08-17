def fast_degree(a,n):
    """ Быстрое рекурсивное возведение в целую степень
    """
    if n == 0:
        return 1
    elif(n % 2 == 1):
        return fast_degree(a,n-1)*a
    else:
        return fast_degree(a**2, n//2)

def test_fd():
    m = fast_degree(2,5)
    print("testcase #1: ","Ok" if m == 32 else "False")
    m = fast_degree(1.5, 100)
    print("testcase #2: ","Ok" if m == 1.5**100 else "False")
    m = fast_degree(2, 1024)
    print("testcase #3: ","Ok" if m == 2**1024 else "False")

test_fd()
