#http://codekata.com/kata/kata11-sorting-it-out/
from typing import Any, Protocol
from collections import deque
from string import ascii_lowercase

DEBUG = False

class Inserter(Protocol):

    def add(self, val: Any) -> None: ...

class Insertion:
    def __init__(self, vals: deque[Any] | None = None) -> None:
        self.vals = vals or deque()

    def add(self, val: Any) -> None:
        if not self.vals:
            self.vals.append(val)
            return
        for idx, ival in enumerate(self.vals):
            if val <= ival:
                self.vals.insert(idx, val)
                return
        self.vals.append(val)

class BInserter:
    def __init__(self, vals: deque[Any] | None = None) -> None:
        self.vals = vals or deque()

    def add(self, val: Any) -> None:
        if not self.vals:
            self.vals.append(val)
            return
        l,r = 0, len(self.vals)
        m = (r+l) // 2
        count = m
        while l <  r and count:
            cur = self.vals[m]
            if DEBUG:
                print(f"\t{l} <= {m} <= {r} iter:{count}")
            if val == cur:
                break
            if val < cur:
                r = m
            else:
                l = m
            count -= 1
            m = (r+l) // 2
        if DEBUG:
            print(f"{l} <= {m} <= {r} iter:{count} {self.vals}")
        self.vals.insert(m+1 if val > self.vals[m] else m, val)

class Sorter:
    def __init__(self, ins: Inserter):
        self.ins: Inserter =  ins

    def add(self, val: str|int ) -> None:
        if type(val) is str:
            val = val.lower()
            if val in ascii_lowercase:
                return self.ins.add(val)
            return
        return self.ins.add(val)

    @property
    def balls(self) -> list[Any]:
        return list(self.ins.vals)

    def __str__(self) -> str:
        return ''.join(map(str, self.ins.vals))

def test_balls(strategy: Inserter):
    sorter = Sorter(strategy)
    assert sorter.balls == []
    sorter.add(20)
    assert sorter.balls == [20]
    sorter.add(10)
    assert sorter.balls == [10, 20]
    sorter.add(30)
    assert sorter.balls == [10, 20, 30]
    sorter.add(50)
    assert sorter.balls == [10, 20, 30, 50]
    sorter.add(10)
    assert sorter.balls == [10, 10, 20, 30, 50]
    sorter.add(5)
    assert sorter.balls == [5, 10, 10, 20, 30, 50]
    sorter.add(15)
    assert sorter.balls == [5, 10, 10, 15, 20, 30, 50]

def test_chars(strategy: Inserter):
    in_str = '''When not studying nuclear physics, Bambi likes to play
beach volleyball.'''
    sorter = Sorter(strategy)
    for s in in_str:
        sorter.add(s)
    assert str(sorter) == 'aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy'

def main():
    test_balls(Insertion())
    test_chars(Insertion())
    test_balls(BInserter())
    test_chars(BInserter())

if __name__ == '__main__':
    main()
