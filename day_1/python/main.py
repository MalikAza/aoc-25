from functools import cache
from io import TextIOWrapper
import re
from typing import List, Literal, TypedDict
from utils.python import solution_print
from utils.python.input import get_input_file_from_script_file

class ParsedRotation(TypedDict):
    rotation: Literal['L', 'R']
    tick: int
    result: int

class Solver:
    pass_by_zero_count: int = 0
    dial: int = 50
    parsed: bool = False
    rotations: List[str]

    def __init__(self, file: TextIOWrapper):
        self.rotations = [line.replace('\n', '') for line in file.readlines()]

    def __parse_rotation(self, rotation: str) -> ParsedRotation:
        pattern = r'^(?P<rotation>[LR])(?P<tick>\d+)$'
        matching = re.match(pattern, rotation)

        if matching:
            rotation: Literal['L', 'R'] = matching.group('rotation')
            tick = int(matching.group('tick'))
            result = -tick if rotation == 'L' else tick

            return {
                'rotation': rotation,
                'tick': tick,
                'result': result
            }

    def __calculate_future_dial_value(self, rotation: str) -> int:
        change = self.__parse_rotation(rotation)
        future = self.dial + change.get('result')

        match change.get('rotation'):
            case 'L':
                self.pass_by_zero_count += ((self.dial - 1) // 100) - ((future - 1) // 100)
            case 'R':
                self.pass_by_zero_count += (future // 100) - (self.dial // 100)
        
        self.dial = future % 100

        return self.dial
    
    def __parse(self) -> None:
        self.ticks_per_rotation = [
            self.__calculate_future_dial_value(rotation)
            for rotation in self.rotations
        ]
        self.parsed = True
        
    def solve(self, part: Literal[1, 2]):
        if not self.parsed:
            self.__parse()

        match part:
            case 1:
                return self.ticks_per_rotation.count(0)
            
            case 2:
                return self.pass_by_zero_count

def run():
    file = get_input_file_from_script_file(__file__)
    solver = Solver(file)

    solution_print(1, solver.solve(1))
    solution_print(2, solver.solve(2))

if __name__ == "__main__":
    run()