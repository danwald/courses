from collections import Counter

def CountingAnagrams(input: str):
    list_dicts = [Counter(item) for item in set(input.split(' '))]
    counts = Counter(hash(frozenset(item.items())) for item in list_dicts)
    return sum( 1 if count >1 else 0 for count in counts.values() )

if __name__ == '__main__':
    print('Test 1 passed: {}'.format(CountingAnagrams('rrdd ddrr') == 1))
    print('Test 2 passed: {}'.format(CountingAnagrams('cars arcs srac cars on no a alla') == 2))
    print('Test 3 passed: {}'.format(CountingAnagrams('a b c d run urn urn') == 1))
    print('Test 4 passed: {}'.format(CountingAnagrams('a b c d run urn urn qwqwwqqwwqqwqw') == 1))
    print('Test 5 passed: {}'.format(CountingAnagrams('a b c d run urn urn aap paa apa lego egol') == 3))
