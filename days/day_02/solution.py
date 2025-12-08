import re
from dataclasses import dataclass
from typing import List

from fraocme import Solver
from fraocme.common import parser


@dataclass
class IDRange:
    min: int
    max: int

    def __has_duplicate(self, id: str) -> bool:
        return bool(re.search(r"^(\d+)\1$", id))

    def __hase_multiple_duplicate(self, id: str) -> bool:
        return bool(re.search(r"^(\d+)\1+$", id))

    def sum_duplicates(self) -> int:
        return sum(
            num if self.__has_duplicate(str(num)) else 0
            for num in range(self.min, self.max + 1)
        )

    def sum_multiple_duplicates(self) -> int:
        return sum(
            num if self.__hase_multiple_duplicate(str(num)) else 0
            for num in range(self.min, self.max + 1)
        )


class Day2(Solver):
    def __init__(self, day: int = 2, **kwargs):
        super().__init__(day=day, **kwargs)

    def parse(self, raw: str) -> List[IDRange]:
        """Parse the input data."""
        ranges = parser.ranges(raw)
        return [IDRange(*range) for range in ranges]

    def part1(self, data: List[IDRange]):
        """Solve part 1."""
        return sum(range.sum_duplicates() for range in data)

    def part2(self, data: List[IDRange]):
        """Solve part 2."""
        return sum(range.sum_multiple_duplicates() for range in data)
