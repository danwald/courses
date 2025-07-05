import tempfile
import codecs
from collections import defaultdict
from pathlib import Path


class Words(defaultdict[int, list[str]]):
    def __init__(self, path: Path = Path("../data/worlist.txt")) -> None:
        self.path = path

    def process(self) -> None:
        pass

    def __str__(self) -> str:
        if not self:
            self.process()
        return f"dictionary size length {sum(len(words) for words in self.values())}"


def dict_word_len_grouped(
    path: str = "../data/wordlist.txt",
) -> defaultdict[int, set[str]]:
    dt: defaultdict[int, set[str]] = defaultdict(set)
    with codecs.open(path, "r", encoding="utf-8", errors="ignore") as fp:
        for line in fp:
            for word in line.strip().split(" "):
                dt[len(word)].add(word)
    return dt


def main() -> None:
    d = dict_word_len_grouped()
    print(f"dictionary size length {sum(len(words) for words in d.values())}")


def tests() -> None:
    with tempfile.NamedTemporaryFile(mode="w+") as tmp:
        tmp.write("cat\ncog\ncot\ndog\n")
        tmp.flush()
        td = dict_word_len_grouped(tmp.name)
        print(f"dictionary size length {sum(len(words) for words in td.values())}")


if __name__ == "__main__":
    tests()
    # main()
