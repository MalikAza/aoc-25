from functools import cache
from io import TextIOWrapper
from itertools import count
import re
from typing import List
from utils.python import solution_print
from utils.python.input import get_input_file_from_script_file

class Solver:
    dial: int = 50
    rotations: List[str]

    def __init__(self, file: TextIOWrapper):
        self.rotations = [line.replace('\n', '') for line in file.readlines()]

    @cache
    def __parse_rotation(self, rotation: str) -> int:
        pattern = r'^(?P<rotation>[LR])(?P<tick>\d+)$'
        matching = re.match(pattern, rotation)

        if matching:
            rotation = matching.group('rotation')
            tick = int(matching.group('tick'))

        if rotation == 'L':
            return - tick
        return tick

    def __calculate_future_dial_value(self, rotation: str) -> int:
        future = self.dial + self.__parse_rotation(rotation)
        if 0 < future < 99:
            self.dial = future
        else:
            self.dial = future % 100

        return self.dial
        
    def solve(self):
        tick_numbers = [
            self.__calculate_future_dial_value(rotation)
            for rotation in self.rotations
        ]

        return tick_numbers.count(0)

def run():
    file = get_input_file_from_script_file(__file__)
    solver = Solver(file)

    solution_print(1, solver.solve())

if __name__ == "__main__":
    run()