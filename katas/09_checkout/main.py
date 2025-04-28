#http://codekata.com/kata/kata09-back-to-the-checkout/

class Checkout:
    def __init__(self,  rules_path: str) -> None:
        self.rules_path = rules_path

    @property
    def total(self) -> float:
        return 0.0

    def scan(self, item: str) -> None:
        pass

def price(items, rules):
    co = Checkout(rules)
    for item in items:
        co.scan(item)
    return co.total

def test_totals(rules):
    assert 0 == price("", rules)
    assert 50 == price("A", rules)
    assert 80 == price("AB", rules)
    assert 115 == price("CDBA", rules)

    assert 100 == price("AA", rules)
    assert 130 == price("AAA", rules)
    assert 180 == price("AAAA", rules)
    assert 230 == price("AAAAA", rules)
    assert 260 == price("AAAAAA", rules)

    assert 160 == price("AAAB", rules)
    assert 175 == price("AAABB", rules)
    assert 190 == price("AAABBD", rules)
    assert 190 == price("DABABA", rules)

def test_incremental(rules):
    co = Checkout(rules)
    assert   0 == co.total
    co.scan("A");  assert  50 == co.total
    co.scan("B");  assert  80 == co.total
    co.scan("A");  assert 130 == co.total
    co.scan("A");  assert 160 == co.total
    co.scan("B");  assert 175 == co.total


def main():
    rules = 'data/prices.csv'
    test_incremental(rules)
    test_totals(rules)

if __name__ == "__main__":
  main()
