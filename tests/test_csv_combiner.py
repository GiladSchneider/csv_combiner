import pytest
# import csv_combiner
from csv_combiner import check_filename, merge_dataframes
import pandas as pd
import os

def test_check_filename_rejects_non_strings():
    with pytest.raises(NameError):
        check_filename(1)
        check_filename(1.0)
        check_filename(True)
        check_filename(False)
        check_filename(None)
        check_filename([1, 2, 3])
        check_filename({'a': 1, 'b': 2})
        check_filename((1, 2, 3))
    
def test_check_filename_rejects_filenames_not_in_fixtures():
    with pytest.raises(FileNotFoundError):
        check_filename("./other_place/clothing.csv")

def test_check_filename_rejects_wrong_format():
    with pytest.raises(ValueError):
        check_filename("./fixtures/clothing.csv.csv")
        check_filename("./fixtures/clothing.csv.")
        check_filename("./fixtures/.csv")
        check_filename("./fixtures/clothing")
    
def test_check_filename_accepts_correct_filenames():
    assert check_filename("./fixtures/clothing.csv") == True
    assert check_filename("./fixtures/accessories.csv") == True
    assert check_filename("./fixtures/household_cleaners.csv") == True

def test_merge_dataframes_merges_correctly():
    df1 = pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']})
    df2 = pd.DataFrame({'email_hash': ['g', 'h', 'i'], 'category': ['j', 'k', 'l']})
    df = merge_dataframes(df1, df2)
    assert df.equals(pd.DataFrame({'email_hash': ['a', 'b', 'c', 'g', 'h', 'i'], 'category': ['d', 'e', 'f', 'j', 'k', 'l']}))

def test_merge_dataframes_merges_correctly_with_none():
    df1 = pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']})
    df = merge_dataframes(df1, None)
    assert df.equals(pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']}))

def test_merge_dataframes_merges_correctly_with_empty_dataframe():
    df1 = pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']})
    df2 = pd.DataFrame()
    df = merge_dataframes(df1, df2)
    assert df.equals(pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']}))

def test_merge_dataframes_merges_correctly_with_empty_dataframe_and_none():
    df1 = pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']})
    df2 = pd.DataFrame()
    df = merge_dataframes(df1, df2)
    assert df.equals(pd.DataFrame({'email_hash': ['a', 'b', 'c'], 'category': ['d', 'e', 'f']}))