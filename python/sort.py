
def msort(alist):
    while len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        msort(left)
        msort(right)

        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

        return alist

def qsort(alist):
    return alist

if __name__ == '__main__':
    alist = [323, 23, 1, 4 ,6, 7, 532, 232]
    mlist = msort(alist.copy())
    print(mlist)
    qlist = qsort(alist.copy())
    print(qlist)
    assert mlist == qlist
