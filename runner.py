import sys
import importlib
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python runner.py <day_number>')
        sys.exit(1)

    day = sys.argv[1]
    day_dir = Path(__file__).parent / f'day_{day}'

    if not day_dir.exists() or not (day_dir / 'main.py').exists():
        print(f'\033[91mNo solution for day \033[93m{day}\033[91m.\033[0m')
        sys.exit(1)

    try:
        module = importlib.import_module(f'day_{day}.main')
        module.run()
    except Exception as e:
        import traceback
        print(f'\033[91mError running day \033[93m{day}\033[91m:\033[0m')
        print('\033[91m', end='')
        traceback.print_exc()
        print('\033[0m', end='')
        sys.exit(1)
