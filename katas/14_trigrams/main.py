import sys
import argparse
from pathlib import Path
import random
from collections import defaultdict


class TriDB(defaultdict[str, list[str]]):
    def __init__(self, infile: Path) -> None:
        self.infile = infile
        super().__init__(list)
        self.gen_db()

    def gen_key(self, a: str, b: str) -> str:
        return f"{a} {b}"

    def gen_db(self) -> None:
        with open(self.infile) as fp:
            for line in fp.readline():
                toks = line.strip().split()
                for i in range(len(toks)):
                    if i == len(toks) - 1:
                        break
                    self[self.gen_key(toks[i], toks[i + 1])] += toks[i + 2]

    def get_next(self, a: str, b: str) -> str:
        if self.gen_key(a, b) in self:
            return random.choice(self[self.gen_key(a, b)])
        return ""

    def get_random_start(self) -> tuple[str, str]:
        key = str(random.choice(self.keys()))  # type: ignore
        a, b = key.split(maxsplit=1)
        return a, b


def main(infile: Path, outfile: Path) -> None:
    db = TriDB(infile)
    a, b = db.get_random_start()
    with open(outfile, "w") as fo:
        while c := db.get_next(a, b):
            fo.write(f"{a} {b} {c}")
            a, b = b, c


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="TextGen", description="Generate text given an input corpus"
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=Path,
        help="corpus to generate trigrams",
        default=sys.stdin,
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        type=Path,
        help="generated output from trigrams",
        default=sys.stdout,
    )
    args = parser.parse_args()
    main(args.infile, args.outfile)
