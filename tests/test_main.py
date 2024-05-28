import sys
from pathlib import Path

sys.path.append(Path.cwd().parent)

from main import main
from find_horse import make_entry_dict
from checking_entry import notify_entry

def test_main():
    entry_dict = make_entry_dict(race_id="201706050811")
    print(entry_dict)
    my_dict = {"キタサンブラック": ""}

    notify_entry(entry_dict=entry_dict, my_dict=my_dict)