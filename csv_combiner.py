
import sys
import os
import pandas as pd

def check_filename(filename):
    """
    Input:
        filename: string -> filename to check 
    Output:
        is_legal: boolean -> True if filename is a legal filename
    """
    # check if filename is a string
    if not isinstance(filename, str):
        return False
    # check if filename is in /fixtures
    if not filename.startswith('./fixtures/'):
        return False
    # check that filename is in the format ./fixtures/<name>.csv
    parts = filename.split(".")
    if len(parts) != 3 or parts[1] == "" or parts[-1] != "csv":
        return False
    return True

def merge_dataframes(df1, df2):
    """
    Input:
        df1: pandas dataframe -> first dataframe to merge
        df2: pandas dataframe -> second dataframe to merge
    Output:
        merged: pandas dataframe -> merged dataframe
    """
    if df2 is None:
        return df1
    else:
        return pd.concat([df1, df2], ignore_index=True)

def main():
    filenames = set("./fixtures/" + s for s in os.listdir("fixtures")) # get all filenames in /fixtures    
    for filename in sys.argv[1:]:           # iterate over all filenames passed in as arguments
        if not check_filename(filename):    # check if filename is legal
            raise NameError(f"file name '{filename}' is not formatted correctly")
        elif filename not in filenames:     # check if filename is in /fixtures
            raise FileNotFoundError(f"file '{filename}' is not in /fixtures") 
    
    # convert all csv files to dataframes
    dataframes = []                         # list of csv files converted to dataframes
    for filename in sys.argv[1:]:
            df = pd.read_csv(filename)                  # convert csv to dataframe              
            df['filename'] = os.path.basename(filename) # add a column to dataframe with the filename's basename            
            dataframes.append(df)                       # add dataframe to list of dataframes
            
    # merge all csv files
    while len(dataframes) > 1:
            merged = []
            for i in range(0, len(dataframes), 2):
                f1 = dataframes[i]
                f2 = dataframes[i+1] if (i+1)<len(dataframes) else None
                merged.append(merge_dataframes(f1, f2))
            dataframes = merged
    # print the full merged dataframe to stdout
    print(dataframes[0].to_csv(index=False))

if __name__ == '__main__':    
    main()