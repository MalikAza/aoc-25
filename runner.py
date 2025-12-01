import sys
from day_1.python.main import run as day_1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python runner.py <day_number>')
        sys.exit(1)

    day = sys.argv[1]

    match day:
        case '1':
            day_1()
        case _:
            print('No solution for this day.')