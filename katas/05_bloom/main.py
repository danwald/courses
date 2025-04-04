'''
http://codekata.com/kata/kata05-bloom-filters/

So, this kata is fairly straightforward. Implement a Bloom filter based spell checker. You’ll need some kind of bitmap, some hash functions, and a simple way of reading in the dictionary and then the words to check. For the hash function, remember that you can always use something that generates a fairly long hash (such as MD5) and then take your smaller hash values by extracting sequences of bits from the result. On a Unix box you can find a list of words in /usr/dict/words (or possibly in /usr/share/dict/words) ...
'''
from typing import Protocol
import random
import itertools
from hashlib import md5

class Hasher(Protocol):
    def hashes(self, data: str, mod :int) -> set[int] | None:
        ...

class MDFiver:
    def __init__(self, times=5):
        self.times = times

    def hashes(self, data: str, mod :int) -> set[int] | None:
        hashes = set()
        digest =  md5(data.encode('utf-8')).digest()
        for i in range(self.times):
            #claude gpt
            # Take 4 bytes at a time (with wrapping) and convert to int
            start_pos = (i * 4) % len(digest)
            # Get 4 bytes and wrap around if needed
            chunk = digest[start_pos:start_pos+4] if start_pos + 4 <= len(digest) else \
                   digest[start_pos:] + digest[:4-(len(digest)-start_pos)]

            # Convert 4 bytes to integer and mod by the bit array size
            value = int.from_bytes(chunk, byteorder='little') % mod
            hashes.add(value)

        return hashes


class Bloomer:
    def __init__(self, size: int=10_000_000,  hasher: Hasher=MDFiver()) -> None:
        self.size = size
        self.filter = [0]*self.size
        self.hasher = hasher

    def load_words(self, file_path='/usr/share/dict/words') -> None:
        self.filter = [0]*self.size
        count = 0
        with open(file_path) as fp:
            for count, word in enumerate(fp):
                word = word.strip()  # Remove newline characters
                for idx in self.hasher.hashes(word, self.size):
                    self.filter[idx] = 1
        print(f'Loaded {count} from ->{file_path}')


    def __contains__(self, word: str):
        hashes = self.hasher.hashes(word, self.size)
        return all(map(lambda idx: self.filter[idx], hashes))


def main():
    mhasher= MDFiver()
    assert mhasher.hashes('hello', 1_000_000) == mhasher.hashes('hello', 1_000_000)
    assert mhasher.hashes('hello', 1_000_000) != mhasher.hashes('hello', 1_000)
    assert mhasher.hashes('hello', 1_000_000) != mhasher.hashes('f00bar', 1_000_000)
    b = Bloomer()
    b.load_words()
    assert 'hello' in b
    assert 'f00bar' not in b


if __name__ == '__main__':
     main()
