import tempfile
import codecs
from collections import defaultdict
from pathlib import Path


class Words(defaultdict[int, set[str]]):
    def __init__(self, path: Path = Path("../data/worlist.txt")) -> None:
        super().__init__(set)
        self.path = path
        if not path.exists():
            raise ValueError(f"Invalid file path {self.path}")

    def process(self) -> None:
        with codecs.open(self.path, "r", encoding="utf-8", errors="ignore") as fp:
            for line in fp:
                for word in line.strip().split(" "):
                    self[len(word)].add(word)

    def __str__(self) -> str:
        if not self:
            self.process()
        return f"dictionary size length {sum(len(words) for words in self.values())}"



def main() -> None:
    d = Words()
    print(f"{d}")


def tests() -> None:
    with tempfile.NamedTemporaryFile(mode="w+") as tmp:
        tmp.write("cat\ncog\ncot\ndog\n")
        tmp.flush()
        td = Words(Path(tmp.name))
        print(f"{td}")


if __name__ == "__main__":
    tests()
    main()
