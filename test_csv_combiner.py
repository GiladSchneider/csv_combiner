import pytest
from src.csv_combiner import check_filename, merge_dataframes
import os
import pandas as pd

def test_check_filename_rejects_non_strings():
    filenames = set("./fixtures/" + s for s in os.listdir("fixtures"))
    with pytest.raises(NameError):
        check_filename(1, filenames)
        check_filename(1.0, filenames)
        check_filename(True, filenames)
        check_filename(None, filenames)
        check_filename([1, 2, 3], filenames)
        check_filename({"a": 1, "b": 2}, filenames)
        check_filename((1, 2, 3), filenames)
    
def test_check_filename_starts_with_fixtures():
    filenames = set("./fixtures/" + s for s in os.listdir("fixtures"))
    with pytest.raises(NameError):
        check_filename("name.csv", filenames)
        check_filename("./name.csv", filenames)
        check_filename("./fixtures2/name.csv", filenames)

def test_check_filename_incorrect_format():
    filenames = set("./fixtures/" + s for s in os.listdir("fixtures"))
    with pytest.raises(NameError):
        check_filename("./fixtures/name", filenames)
        check_filename("./fixtures/name.", filenames)
        check_filename("./fixtures/name.txt", filenames)
        check_filename("./fixtures/name.csv.txt", filenames)
        check_filename("./fixtures/.csv", filenames)

def test_check_filename_not_in_fixtures():
    filenames = set("./fixtures/" + s for s in os.listdir("fixtures"))
    with pytest.raises(FileNotFoundError):
        check_filename("./fixtures/not_in_fixtures.csv", filenames)

def test_check_filename_empty():
    def create_empty_file(filename):
        with open(filename, "w") as f:
            pass

    create_empty_file("./fixtures/empty8932473489437294.csv")
    filenames = set("./fixtures/" + s for s in os.listdir("fixtures"))
    with pytest.raises(ValueError):
        check_filename("./fixtures/empty8932473489437294.csv", filenames)
    os.remove("./fixtures/empty8932473489437294.csv")

def test_merge_dataframes_empty():
    assert merge_dataframes(None, None) is None
    assert merge_dataframes(pd.DataFrame(), pd.DataFrame()) is not None
    assert merge_dataframes(pd.DataFrame(), None) is not None