def get_non_adj_ones(bits: int) -> int:
    if bits < 0:
        raise ValueError(f"#bits {bits} should be +ve integer")
    mxx = 2**bits
    count = 0
    for i in range(mxx + 1):
        while i:
            bs = f"{i:b}"
            print(bs)
            i = i >> 1
    return count


if __name__ == "__main__":
    try:
        get_non_adj_ones(-1)
        assert False
    except Exception as e:
        assert isinstance(e, ValueError)

    assert 1 == get_non_adj_ones(1)
    assert 3 == get_non_adj_ones(2)
