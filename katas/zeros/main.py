# list of zeros move zero to one end of list


def move_inplace(array):
    def next_val(array, idx, val, neg=False):
        while idx < len(array):
            ev = array[idx] == val
            if neg:
                ev = not ev
            if ev:
                break
            else:
                idx += 1
        return idx if idx < len(array) else idx - 1

    if len(array) < 2:
        return array

    def swap(array, i, j, swap=True):
        if swap:
            array[i], array[j] = array[j], array[i]
        else: # head insert
            assert i < j
            iv = array[j]
            array[i+1:j+1] = array[i:j]
            array[i] = iv

    i = 1
    while i < len(array):
        pi = i-1
        #print(array, pi, i)
        pv, nv = array[pi], array[i]
        if pv:
            if not nv:
                swap(array, pi, i, False)
            else:
                j = next_val(array, i, 0)
                #print(j)
                if not array[j]:
                    swap(array, pi, j, False)
        i += 1
    return array


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

    z, i = [], []
    for x in array:
        if not x:
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
        print(f'testing: {mt.__name__}')
        #assert [] ==  mt([])
        #assert [0] ==  mt([0])
        #assert [0,1] ==  mt([1,0])
        #assert [0,1] ==  mt([0,1])
        #assert [0,0,1,2] ==  mt([1,2,0,0])
        #assert [0,0,0,0] ==  mt([0,0,0,0])
        #assert [0,0,1,2] ==  mt([0,0,1,2])
        #assert [3,4,1,2] ==  mt([3,4,1,2])
        #assert [0,0,1,2] ==  mt([0,1,0,2])
        assert [0,0,0,0,1,2,3,5] ==  mt([0,1,2,0,0,3,0,5])
