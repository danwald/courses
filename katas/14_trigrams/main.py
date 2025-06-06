import sys
import argparse
import random
from collections import defaultdict
from io import TextIOWrapper


class TriDB(defaultdict[str, list[str]]):
    def __init__(self, infile: TextIOWrapper) -> None:
        self.infile = infile
        super().__init__(list)
        self._gen_db()

    def gen_key(self, a: str, b: str) -> str:
        return f"{a} {b}"

    def _gen_db(self) -> None:
        for line in self.infile:
            toks = line.strip().split()
            if len(toks) < 3:
                continue
            for i in range(len(toks)):
                if i == len(toks) - 2:
                    break
                self[self.gen_key(toks[i], toks[i + 1])].append(toks[i + 2])
        print(self)
        self.infile.close()

    def __str__(self) -> str:
        return f"{len(self)} bi-grams"

    def get_next(self, a: str, b: str) -> str:
        if self.gen_key(a, b) in self:
            return random.choice(self[self.gen_key(a, b)])
        return ""

    def get_random_start(self) -> tuple[str, str]:
        key = random.choice(list(self.keys()))
        a, b = key.split(maxsplit=1)
        return a, b


def main(infile: TextIOWrapper, outfile: TextIOWrapper) -> None:
    db = TriDB(infile)
    a, b = db.get_random_start()
    try:
        while c := db.get_next(a, b):
            outfile.write(f"{c} ")
            a, b = b, c
    except Exception:
        pass
    finally:
        outfile.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="TextGen", description="Generate text given an input corpus"
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        help="corpus to generate trigrams (default:stdin)",
        default=sys.stdin,
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        type=argparse.FileType("w"),
        help="generated output from trigrams (default:stdout",
        default=sys.stdout,
    )
    args = parser.parse_args()
    main(args.infile, args.outfile)
