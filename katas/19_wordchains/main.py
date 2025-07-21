import tempfile
import codecs
from collections import defaultdict
from pathlib import Path
from ldistance import distance


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

    def chain(self, start: str, end: str) -> list[list[str]]:
        if not (start or end) or len(start) != len(end):
            raise ValueError(
                f"Invalid start:'{start}' or end:'{end}' words. Empty or not same length"
            )
        if not self:
            self.process()

        sol: list[str] = []
        result: list[list[str]] = []

        def bt(word: str) -> bool:
            if word == end:
                result.append(sol[:])
                return True
            if word in sol:
                return False

            candidates = (cw for cw in self[len(word)] if distance(word, cw) == 1)
            sol.append(word)
            for cw in candidates:
                sol.append(cw)
                bt(cw)
                sol.pop()
            sol.pop()
            return False

        bt(start)
        return result


def main() -> None:
    d = Words()
    print(f"{d}")


def tests() -> None:
    with tempfile.NamedTemporaryFile(mode="w+") as tmp:
        tmp.write("cat\ncog\ncot\ndog\n")
        tmp.flush()
        td = Words(Path(tmp.name))
        print(f"{td}")
        print(td.chain("cog", "dog"))
        print(td.chain("cat", "dog"))


if __name__ == "__main__":
    tests()
    # main()
