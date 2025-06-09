import sys
import argparse
import random
from collections import defaultdict
from io import TextIOWrapper
import time


class TriDB(defaultdict[str, list[str]]):
    def __init__(self, infile: TextIOWrapper) -> None:
        self.infile = infile
        super().__init__(list)
        start = time.perf_counter()
        self._gen_db()
        end = time.perf_counter()
        print(f"{self} in {end - start:.4f} seconds")

    def gen_key(self, a: str, b: str) -> str:
        return f"{a} {b}"

    def _gen_db(self) -> None:
        for line in self.infile:
            toks = line.strip().split()
            if len(toks) < 3:
                continue
            for i in range(len(toks) - 2):
                self[self.gen_key(toks[i], toks[i + 1])].append(toks[i + 2])
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


def main(
    infile: TextIOWrapper,
    outfile: TextIOWrapper,
    min_length: int = 300,
    backtracks: int = 10,
) -> None:
    db = TriDB(infile)
    bt: list[tuple[str, str]] = list()
    a, b = db.get_random_start()
    try:
        for i in range(min_length):
            c = db.get_next(a, b)
            if not c:
                backtracks -= 1
                a, b = random.choice(bt) if bt else db.get_random_start()
                continue
            outfile.write(f"{c} ")
            bt.append((a, b))
            a, b = b, c
            if not backtracks:
                break
    except Exception:
        pass
    finally:
        print(f"\n{i} words with {backtracks} backtracks remaining")
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
    parser.add_argument(
        "--min-length",
        type=int,
        help="minimum output length (default:300)",
        default=300,
    )
    parser.add_argument(
        "--backtracks",
        type=int,
        help="max number of backtracks incase of not found (default:10)",
        default=10,
    )
    args = parser.parse_args()
    main(
        args.infile,
        args.outfile,
        min_length=args.min_length,
        backtracks=args.backtracks,
    )
