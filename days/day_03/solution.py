from typing import List

from fraocme import Solver
from fraocme.common import parser


class Bank:
    batteries: List[str]

    def __init__(self, line: str):
        self.batteries = [c for c in line]

    def get_max_joltage(self, count: int) -> int:
        if count == len(self.batteries):
            return int("".join(self.batteries))

        indices = []
        skip_count = len(self.batteries) - count
        position = 0  # noqa: F811

        for i in range(count):
            max_position = len(self.batteries) - (count - i)
            best_position = position

            for j in range(position, max_position + 1):
                if self.batteries[j] > self.batteries[best_position]:
                    best_position = j

            indices.append(best_position)
            skip_count -= best_position - position
            position = best_position + 1

        return int("".join(self.batteries[i] for i in indices))


class Day3(Solver):
    def __init__(self, day: int = 3, **kwargs):
        super().__init__(day=day, **kwargs)

    def parse(self, raw: str) -> List[Bank]:
        """Parse the input data."""
        lines = parser.lines(raw)
        return [Bank(line) for line in lines]

    def part1(self, data: List[Bank]):
        """Solve part 1."""
        return sum(bank.get_max_joltage(2) for bank in data)

    def part2(self, data: List[Bank]):
        """Solve part 2."""
        return sum(bank.get_max_joltage(12) for bank in data)
