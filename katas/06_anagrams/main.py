#http://codekata.com/kata/kata06-anagrams/
# only considers ascii chars
# recommend result is waay lower 20683 sets of anagrams (a total of 48162 words)

from collections import defaultdict, Counter
import string
import codecs

class AnagramSets:
    LOWER_LETTERS = set(string.ascii_lowercase)
    def __init__(self) -> None:
        self.anagram_dict = defaultdict(set)

    @classmethod
    def from_file(cls, path):
        ana = cls()
        with codecs.open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                for word in line.strip().split(' '):
                    ana.add(word)
        return ana

    def add(self, word: str) -> None:
        key = self.get_anagram_key(word)
        self.anagram_dict[key].add(word)

    @staticmethod
    def get_anagram_key(word: str) -> str:
        cnts = Counter(word.lower())
        cnt_str = [0]*26
        for letter, count in cnts.items():
            if letter in AnagramSets.LOWER_LETTERS:
                cnt_str[ord(letter) - ord('a')] += count
        return ''.join(str(val) for val in cnt_str)

    def __len__(self) -> int:
        return sum(1 for _,v in self.anagram_dict.items() if len(v) > 1)

    @property
    def words(self) -> int:
        return sum(len(val) for val in self.anagram_dict.values())

    def __str__(self):
        return f"{len(self.anagram_dict)} Anagram sets with {self.words} words"

def main():
    test_set = AnagramSets.from_file('wordlist-test.txt')
    assert len(test_set) == 11
    print(test_set)
    print(AnagramSets.from_file('wordlist.txt'))


if __name__ == "__main__":
    main()
