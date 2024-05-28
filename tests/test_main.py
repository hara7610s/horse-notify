import sys
from pathlib import Path

sys.path.append(Path.cwd().parent)

from main import main

def test_main():
    main(debug=True)