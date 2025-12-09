from typing import List

from fraocme import Solver
from fraocme.grid import Grid, Position
from fraocme.grid import parser as grid_parser


class Day4(Solver):
    def __init__(self, day: int = 4, **kwargs):
        super().__init__(day=day, **kwargs)

    def __get_paper_rolls_positions(self, grid: Grid[str]) -> List[Position]:
        return grid.find("@")

    def __get_neighbor_paper_roll_count(self, grid: Grid[str], pos: Position) -> int:
        neighbor_values = [n[1] for n in grid.get_neighbor_values(pos)]
        self.debug("neighbor values: ", neighbor_values)
        count = neighbor_values.count("@")
        self.debug("count: ", count)
        return count

    def parse(self, raw: str) -> Grid[str]:
        """Parse the input data."""
        return grid_parser.from_chars(raw)

    def part1(self, data: Grid[str]):
        """Solve part 1."""
        available_paper_roll_count = 0
        paper_rolls_positions = self.__get_paper_rolls_positions(data)

        for pos in paper_rolls_positions:
            paper_roll_count = self.__get_neighbor_paper_roll_count(data, pos)
            self.debug("paper roll count: ", paper_roll_count)
            if paper_roll_count < 4:
                available_paper_roll_count += 1

        return available_paper_roll_count

    def part2(self, data):
        """Solve part 2."""
        return None
