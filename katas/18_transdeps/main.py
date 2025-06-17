# http://codekata.com/kata/kata18-transitive-dependencies/

from collections import defaultdict
from typing import Any


class Deps(defaultdict[str, list[str]]):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(list, *args, **kwargs)

    def add_direct(self, k: str, *deps: str) -> None:
        for d in deps:
            self[k] += d

    def dependencies_for(self, k: str) -> list[str] | None:
        return self.get(k)


def test() -> None:
    dep = Deps()
    dep.add_direct("A", "B", "C")
    dep.add_direct("B", "C", "E")
    dep.add_direct("C", "G")
    dep.add_direct("D", "A", "F")
    dep.add_direct("E", "F")
    dep.add_direct("F", "H")

    assert [
        "B",
        "C",
        "E",
        "F",
        "G",
        "H",
    ] == dep.dependencies_for("A")
    assert [
        "C",
        "E",
        "F",
        "G",
        "H",
    ] == dep.dependencies_for("B")
    assert [
        "G",
    ] == dep.dependencies_for("C")
    assert [
        "A",
        "B",
        "C",
        "E",
        "F",
        "G",
        "H",
    ] == dep.dependencies_for("D")
    assert [
        "F",
        "H",
    ] == dep.dependencies_for("E")
    assert [
        "H",
    ] == dep.dependencies_for("F")


if __name__ == "__main__":
    test()
