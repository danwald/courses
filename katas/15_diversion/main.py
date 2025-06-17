from itertools import pairwise


def get_non_adj_ones(bits: int) -> int:
    if bits < 0:
        raise ValueError(f"#bits {bits} should be +ve integer")
    mxx = 2**bits - 1
    count = 0
    # print(bits, mxx)
    for i in range(mxx + 1):
        bs = f"{i:b}"
        for a, b in pairwise(bs):
            if a == "1" and b == "1":
                # print(bs)
                break
        else:
            count += 1
            # print(bs, count)
    return count


if __name__ == "__main__":
    try:
        get_non_adj_ones(-1)
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)

    assert 2 == get_non_adj_ones(1)
    assert 3 == get_non_adj_ones(2)
    assert 5 == get_non_adj_ones(3)
    assert 8 == get_non_adj_ones(4)
