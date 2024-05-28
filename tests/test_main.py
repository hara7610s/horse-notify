import sys
from pathlib import Path

sys.path.append(Path.cwd().parent)

from scraping_utils import find_horses
from messaging_utils import search_and_notify_entry

def test_main():
    entry_dict = find_horses(race_id="201706050811")
    my_dict = {"キタサンブラック".encode("utf-8"): ""}

    search_and_notify_entry(entry_dict=entry_dict, my_dict=my_dict)