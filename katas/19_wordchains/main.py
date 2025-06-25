import codecs
from collections import defaultdict


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
    pass


if __name__ == "__main__":
    main()
