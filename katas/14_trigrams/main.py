import sys
import argparse
from pathlib import Path


def main(infile: Path, outfile: Path) -> None:
    with open(infile) as fi:
        with open(outfile, "w") as fo:
            for line in fi.readline():
                fo.write(line)


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
