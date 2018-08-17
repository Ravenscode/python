def cycle_left_shift(A:list, N:int):
    """
        Циклический сдвиг на 1 элемент влево
    """
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp

def cycle_right_shift(A:list, N:int):
    """
        Циклический сдвиг на 1 элемент вправо
    """
    tmp = A[N-1]
    for k in range(N-2,-1,-1):
        A[k+1] = A[k]
    A[0] = tmp

def test_cycle_shift():
    A1 = [1,2,3,4,5]
    print(A1)
    cycle_left_shift(A1,5)
    print(A1)
    if A1 == [2,3,4,5,1]:
        print("test1 - ok")
    else:
        print("test1 - fail")

    A2 = [1,2,3,4,5]
    print(A2)
    cycle_right_shift(A2,5)
    print(A2)
    if A2 == [5,1,2,3,4]:
        print("test2 - ok")
    else:
        print("test2 - fail")

test_cycle_shift()
