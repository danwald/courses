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

    def chain(self, start: str, end: str) -> list[list[str]] | None:
        if not (start or end) or len(start) != len(end):
            raise ValueError(
                f"Invalid start:'{start}' or end:'{end}' words. Empty or not same length"
            )
        if not self:
            self.process()

        sol: list[str] = []
        result: list[list[str]] = []

        def bt(word: str) -> None:
            if word == end:
                sol.append(end)
                result.append(sol[:])
                return
            sol.append(word)
            candidates = list(
                cw
                for cw in self[len(word)]
                if cw not in sol and distance(word, cw) == 1
            )
            # print(f"{word} -> ({candidates}) = {sol} < = {self[len(word)]}")
            for cw in candidates:
                bt(cw)
                sol.pop()
            return

        bt(start)
        return result or None


def main() -> None:
    d = Words()
    print(f"{d}")


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
    # main()
