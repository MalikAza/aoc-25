import sys
import importlib
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python runner.py <day_number>')
        sys.exit(1)

    day = sys.argv[1]
    day_dir = Path(__file__).parent / f'day_{day}' / 'python'

    if not day_dir.exists() or not (day_dir / 'main.py').exists():
        print(f'No solution for day {day}.')
        sys.exit(1)

    try:
        module = importlib.import_module(f'day_{day}.python.main')
        module.run()
    except Exception as e:
        print(f'Error running day {day}: {e}')
        sys.exit(1)
