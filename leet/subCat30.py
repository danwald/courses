from collections import defaultdict, Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        def check1(pre, ix, six):
            found_once = False
            ppos = six
            while True:
                for idx, word in enumerate(words):
                    if idx in ix:
                        continue
                    ppos = s.find(f'{pre}{word}', six)
                    if ppos != -1:
                        if ppos != six:
                            continue
                        pre = f'{pre}{word}'
                        ix.add(idx)
                        found_once = True
                    else:
                        if not found_once:
                            found_once = False
                if not found_once:
                    break
                found_once = False
            #print(f'\t{pre} {len(ix) == len(words)} {ppos} {ix}')
            return ppos if len(ix) == len(words) else -1


        idxs = []
        word_len = sum(len(word) for word in words)
        for ix, word in enumerate(words):
            six=-1
            while (six:=s.find(word, six+1)) != -1:
                #print(word, six)
                if (len(s) - six) >= word_len:
                    idxs.append(check1(word, {ix}, six))

        val = list(set(filter(lambda x: x > -1, idxs)))
        return val

if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo","bar"])) # [0,9]
    #print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])) # []
    #print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6,9,12]
    #print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])) # [8]
    #print(s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])) # [13]
    from data import slow_30_001 as sl001
    #print(s.findSubstring(sl001.s, sl001.words)) # [8]
