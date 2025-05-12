#http://codekata.com/kata/kata11-sorting-it-out/
from typing import Any
class Sorter:
    def __init__(self):
        self.values :list[Any] = []

    def add(self, val: Any) -> None:
        pass

    @property
    def balls(self) -> list[Any]:
        return self.values

    def __str__(self) -> str:
        return ''.join(map(str, self.values))

def test_balls():
    sorter = Sorter()
    assert sorter.balls == []
    sorter.add(20)
    assert sorter.balls == [20]
    sorter.add(10)
    assert sorter.balls == [10, 20]
    sorter.add(30)
    assert sorter.balls == [10, 20, 30]

def test_chars():
    in_str = '''When not studying nuclear physics, Bambi likes to play
beach volleyball.'''
    sorter = Sorter()
    for s in in_str:
        sorter.add(s)
    assert str(sorter) == 'aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy'

def main():
    test_balls()
    test_chars()

if __name__ == '__main__':
    main()
