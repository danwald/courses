from collections import Counter


def main(st: str) -> bool:
    counts = Counter(st)
    if len(counts) == 1:
        return True
    for c in counts.values():
        if c % 2 != 0:
            return False
    return True





if __name__ == "__name__":
    assert main("") == True
    assert main("aaabbba") == True
    assert main("abccba") == True
    assert main("abcbca") == True
    assert main("aaa") == True
    assert main("aba") == False
    assert main("abccab") == False
