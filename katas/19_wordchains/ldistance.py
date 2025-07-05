import sys


def distance(s: str, t: str) -> int:
    # https://en.wikipedia.org/wiki/Levenshtein_distance#Definition
    if not s:
        return len(t)
    if not t:
        return len(s)

    if s[0] == t[0]:
        return distance(s[1:], t[1:])

    return 1 + min(
        distance(s[1:], t),
        distance(s, t[1:]),
        distance(s[1:], t[1:]),
    )


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"{distance(sys.argv[1], sys.argv[2])}")
        sys.exit(0)

    assert distance("foo", "foo") == 0
    assert distance("kitten", "sitting") == 3
    assert distance("foo", "bar") == 3
    assert distance("baz", "bar") == 1
    assert distance("foo", "") == 3
    assert distance("", "bar") == 3
    assert distance("foo", "far") == 2
    assert distance("", "") == 0
