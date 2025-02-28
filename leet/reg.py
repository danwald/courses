class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si,prev,cs,eos = iter(s), '','', False
        adv = True
        for idx, ch in enumerate(p):
            try:
                if adv:
                    prev, cs = cs, next(si)
                    print(f'p:"{prev}", c:"{cs}", r:"{ch}"')
                else:
                    adv = True
            except StopIteration:
                eos = True
                break
            match ch:
                case '.':
                    continue
                case '*':
                    try:
                        while prev == cs:
                            prev, cs = cs, next(si)
                            adv = False
                    except StopIteration:
                        eos = True
                        break
                case _:
                    if ch != cs:
                        if idx:
                            break
        print(cs, prev, eos, idx, len(p)-1)
        return False if not eos else True

#assert Solution().isMatch("aa", "a") == False
#assert Solution().isMatch("aa", "a*") == True
#assert Solution().isMatch("aa", "*") == False
assert Solution().isMatch("ab", ".*") == True
#assert Solution().isMatch("mississippi", "mis*is*ip*.") == True
