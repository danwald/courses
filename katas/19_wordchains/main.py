import tempfile
import codecs
from collections import defaultdict
from pathlib import Path
from ldistance import distance
from itertools import chain
from collections import deque


class Words(defaultdict[int, set[str]]):
    def __init__(self, path: Path = Path("../data/wordlist.txt")) -> None:
        super().__init__(set)
        self.path = path
        if not path.exists():
            raise ValueError(f"Invalid file path {self.path}")

    def process(self) -> None:
        with codecs.open(str(self.path), "r", encoding="utf-8", errors="ignore") as fp:
            for line in fp:
                for word in line.strip().split(" "):
                    self[len(word)].add(word)

    def __str__(self) -> str:
        if not self:
            self.process()
        return f"dictionary size length {sum(len(words) for words in self.values())}"

    def chain(
        self, start: str, end: str, debug: bool = False
    ) -> list[list[str]] | None:
        if not (start or end) or len(start) != len(end):
            raise ValueError(
                f"Invalid start:'{start}' or end:'{end}' words. Empty or not same length"
            )
        if not self:
            self.process()

        if debug:
            paths = len([w for w in self[len(start)] if distance(start, w) == 1])
            print(f"'{start}':{paths} candidate word paths")

        result: list[list[str]] = []
        stack: deque[tuple[str, list[str]]] = deque([(start, [])])

        while stack:
            current_word, path = stack.pop()

            if current_word == end:
                result.append(path + [end])
                continue

            new_path = [p for p in chain(path, [current_word])]
            new_path_set = set(new_path)
            candidates = [
                can_wrd
                for can_wrd in self[len(current_word)]
                if can_wrd not in new_path_set and distance(current_word, can_wrd) == 1
            ]

            for cw in candidates:
                stack.appendleft((cw, new_path[:]))
            if debug:
                print(f"\rpaths: {len(stack)} Found: {len(result)}", end="")

        return result or None


def main() -> None:
    d = Words()
    print(f"{d}")
    assert d.chain("cog", "dog", debug=True) == [["cog", "dog"]]


def tests() -> None:
    with tempfile.NamedTemporaryFile(mode="w+") as tmp:
        tmp.write("cat\ncog\ncot\ndog\nbot")
        tmp.flush()
        td = Words(Path(tmp.name))
        assert td.chain("cog", "dog") == [["cog", "dog"]]
        assert td.chain("cat", "dog") == [
            ["cat", "cot", "cog", "dog"],
            ["cat", "bat", "bot", "cot", "cog", "dog"],
        ] or [["cat", "bat", "bot", "cot", "cog", "dog"], ["cat", "cot", "cog", "dog"]]

        assert td.chain("dog", "cat") == [
            ["dog", "cog", "cot", "bot", "bat", "cat"],
            ["dog", "cog", "cot", "cat"],
        ] or [["dog", "cog", "cot", "cat"], ["dog", "cog", "cot", "bot", "bat", "cat"]]

        assert td.chain("dog", "pat") is None


if __name__ == "__main__":
    tests()
    main()
