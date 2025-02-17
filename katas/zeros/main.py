# list of zeros move zero to one end of list


def move_inplace(array):
    return []


def move_zeros(array):
    match len(array):
        case 0:
            return []
        case 1:
            return array
        case 2:
            if array[1] == 0:
                return [array[1], array[0]]
            else:
                return array

    z, i = [],[]
    for x in array:
        if x == 0:
            z.append(x)
        else:
            i.append(x)
    z.extend(i)
    return z



if __name__ == '__main__':
    for mt in (
        move_zeros,
        move_inplace,
    ):
        assert [] ==  mt([])
        assert [0] ==  mt([0])
        assert [0,1] ==  mt([1,0])
        assert [0,1] ==  mt([0,1])
        assert [0,0,1,2] ==  mt([1,2,0,0])
        assert [0,0,0,0] ==  mt([0,0,0,0])
        assert [0,0,1,2] ==  mt([0,0,1,2])
        assert [3,4,1,2] ==  mt([3,4,1,2])
