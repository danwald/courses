from collections import Counter

def main(moves: list[str]) -> bool:
    if not moves:
        return True

    cm = Counter(moves)
    return cm['U'] == cm['D'] and cm['L'] == cm['R']

if __name__ == '__main__':
    assert main("") == True
    assert main("UD") == True
    assert main("LR") == True
    assert main("UDLRRLDU") == True
    assert main("UULR") == False
    assert main("DDDD") == False
    assert main("LRRLR") == False
