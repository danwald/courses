#http://codekata.com/kata/kata02-karate-chop/
'''
Write a binary chop method that takes an integer search target and a sorted array of integers.
It should return the integer index of the target in the array, or -1 if the target is not in the array.
'''


def iterative_chop(target, array):
    return 0


if __name__ == '__main__':
    for meth in (iterative_chop,):
        assert -1 ==  meth(3, [])
        assert -1 ==  meth(3, [1])
        assert 0 ==  meth(1, [1])
        assert 0 ==  meth(1, [1, 3, 5])
        assert 1 ==  meth(3, [1, 3, 5])
        assert 2 ==  meth(5, [1, 3, 5])
        assert -1 ==  meth(0, [1, 3, 5])
        assert -1 ==  meth(2, [1, 3, 5])
        assert -1 ==  meth(4, [1, 3, 5])
        assert -1 ==  meth(6, [1, 3, 5])
        assert 0 ==  meth(1, [1, 3, 5, 7])
        assert 1 ==  meth(3, [1, 3, 5, 7])
        assert 2 ==  meth(5, [1, 3, 5, 7])
        assert 3 ==  meth(7, [1, 3, 5, 7])
        assert -1 ==  meth(0, [1, 3, 5, 7])
        assert -1 ==  meth(2, [1, 3, 5, 7])
        assert -1 ==  meth(4, [1, 3, 5, 7])
        assert -1 ==  meth(6, [1, 3, 5, 7])
        assert -1 ==  meth(8, [1, 3, 5, 7])
