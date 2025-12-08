import re
from typing import List, Literal, TypedDict

from fraocme import Solver
from fraocme.common import parser


class ParsedRotation(TypedDict):
    rotation: Literal["L", "R"]
    tick: int
    result: int


class Day1(Solver):
    dial: int = 50
    pass_by_zero_count: int = 0
    parsed: bool = False

    def __init__(self, day: int = 1, **kwargs):
        super().__init__(day=day, **kwargs)

    def parse(self, raw: str):
        """Parse the input data."""
        return parser.lines(raw)

    def __parse_rotation(self, rotation: str) -> ParsedRotation:
        pattern = r"^(?P<rotation>[LR])(?P<tick>\d+)$"
        matching = re.match(pattern, rotation)

        if matching:
            rotation: Literal["L", "R"] = matching.group("rotation")
            tick = int(matching.group("tick"))
            result = -tick if rotation == "L" else tick

            return {"rotation": rotation, "tick": tick, "result": result}

    def __calculate_future_dial_value(self, rotation: str) -> int:
        change = self.__parse_rotation(rotation)
        future = self.dial + change.get("result")

        match change.get("rotation"):
            case "L":
                self.pass_by_zero_count += ((self.dial - 1) // 100) - (
                    (future - 1) // 100
                )
            case "R":
                self.pass_by_zero_count += (future // 100) - (self.dial // 100)

        self.dial = future % 100

        return self.dial

    def __parse(self, data: List[str]) -> None:
        self.ticks_per_rotation = [
            self.__calculate_future_dial_value(rotation) for rotation in data
        ]

        self.parsed = True

    def part1(self, data: List[str]):
        """Solve part 1."""
        if not self.parsed:
            self.__parse(data)

        return self.ticks_per_rotation.count(0)

    def part2(self, data: List[str]):
        """Solve part 2."""
        if not self.parsed:
            self.__parse(data)

        return self.pass_by_zero_count
