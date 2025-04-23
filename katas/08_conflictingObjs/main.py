#http://codekata.com/kata/kata08-conflicting-objectives/

import sys
import argparse
import pathlib
from typing import Generator
import codecs

class ConflictingObjectives:
    def __init__(self, words_path: pathlib.Path) ->None:
        self.word_path = words_path

    def word_from_file(self) -> Generator[str]:
        with codecs.open(
            self.word_path, encoding='utf-8', errors='ignore'
        ) as fp:
            for line in fp:
                yield line.strip()

    def get_all_words_set(self) -> set[str]:
        words = set()
        for word in self.word_from_file():
            words.add(word.strip())
        print(f"Read {len(words)} words")
        return words


    def get_words_segments(self, word_len=6) -> dict[str, set]:
        ret = {'words': set(), 'segments': set()}
        count = 0
        for count, word in enumerate(self.word_from_file()):
            match (len(word) == word_len, 1<= len(word) < word_len):
                case (True, False):
                    ret['words'].add(word)
                case (False, True):
                    ret['segments'].add(word)
        print(
            f"Read {len(ret['words'])} of {count} {word_len} letter words ({1-len(ret['words'])/count:.2%} of mem saved). ",
            f"\nRead {len(ret['segments'])} segments",
        )
        return ret

    def get_word_splits(self,word) -> list[tuple[str,str]]:
        ret = []
        wl = len(word)
        for pivot in range(1, wl):
            ret.append(tuple([word[:pivot], word[pivot-wl:]]))
        return ret

    def readable(self) -> None:
        words = self.get_all_words_set()
        for word in filter(lambda x: len(x) == 6, words):
            for prefix, suffix in self.get_word_splits(word):
                if prefix in words and suffix in words:
                    if word.startswith(suffix):
                        prefix, suffix = suffix, prefix
                    print(f"'{prefix}' + '{suffix}' => {word}")


    def optimized(self) -> None:
        word_segs = self.get_words_segments()
        words, segs = word_segs['words'], word_segs['segments']
        for word in words:
            for pre,suf in self.get_word_splits(word):
                if pre in segs and suf in segs:
                    if word.startswith(suf):
                        pre, suf = suf, pre
                    print(f"'{pre}' + '{suf}' => {word}")

    def extendable(self, word_len=6) -> None:
        word_segs = self.get_words_segments(word_len=word_len)
        words, segs = word_segs['words'], word_segs['segments']
        for word in words:
            for pre,suf in self.get_word_splits(word):
                if pre in segs and suf in segs:
                    if word.startswith(suf):
                        pre, suf = suf, pre
                    print(f"'{pre}' + '{suf}' => {word}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('inpath', type=pathlib.Path)
    parser.add_argument('method', choices=('red', 'opt', 'ext'))
    args = parser.parse_args()
    co = ConflictingObjectives(args.inpath)
    match args.method:
        case 'red':
            co.readable()
        case 'opt':
            co.optimized()
        case 'ext':
            co.extendable()


if __name__ == '__main__':
    main()
