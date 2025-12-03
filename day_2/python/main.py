from dataclasses import dataclass
from io import TextIOWrapper
import re
from typing import List, Literal
from utils.python import solution_print
from utils.python.input import get_input_file_from_script_file

@dataclass
class IDRange:
    min: int
    max: int

    def _has_duplicate(self, id: str) -> bool:
        return bool(re.search(r'^(\d+)\1$', id))
    
    def _has_multiple_duplicate(self, id: str) -> bool:
        return bool(re.search(r'^(\d+)\1+$', id))

    def sum_duplicates(self) -> int:
        return sum(
            num if self._has_duplicate(str(num)) else 0
            for num
            in range(self.min, self.max + 1)
        )
    
    def sum_multiple_duplicates(self) -> int:
        return sum(
            num if self._has_multiple_duplicate(str(num)) else 0
            for num
            in range(self.min, self.max + 1)
        )

class Solver:
    ranges: List[IDRange]

    def __init__(self, file: TextIOWrapper):
        self.ranges = [
            IDRange(*tuple(map(int, line.strip().split('-'))))
            for line
            in file.read().split(',')
        ]

    def solve(self, part: Literal[1, 2]) -> int:
        match part:
            case 1:
                return sum(range.sum_duplicates() for range in self.ranges)
            case 2:
                return sum(range.sum_multiple_duplicates() for range in self.ranges)

def run():
    file = get_input_file_from_script_file(__file__)
    solver = Solver(file)

    solution_print(1, lambda: solver.solve(1))
    solution_print(2, lambda: solver.solve(2))

if __name__ == '__main__':
    run()