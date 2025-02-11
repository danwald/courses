#http://codekata.com/kata/kata02-karate-chop/
'''
Write a binary chop method that takes an integer search target and a sorted array of integers.
It should return the integer index of the target in the array, or -1 if the target is not in the array.
'''


def iterative_chop(target, array):
    for i, val in enumerate(array):
        if val == target:
            return i
    return -1

def recursive_chop(target, array):
    def _chop(target, start, end, array):
        if start >= end:
            return -1
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        if start == mid:
            return -1
        if array[mid] < target:
            return _chop(target, mid, end, array)
        else:
            return _chop(target, start, mid, array)
    return _chop(target, 0, len(array), array)


if __name__ == '__main__':
    for meth in (
        iterative_chop,
        recursive_chop,
    ):
        print('Testing', meth.__name__)
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
