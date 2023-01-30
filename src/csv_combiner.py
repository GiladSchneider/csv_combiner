import sys
import os
import pandas as pd

def check_filename(filename, filenames):
    """
    Input:
        filename: string -> filename to check 
        filenames: set -> set of all filenames in /fixtures
    Output:
        True if filename is legal, else raises an error
    """
    # check that filename is a string
    if not isinstance(filename, str):
        raise NameError(f"file name '{filename}' is not a string")

    # check that the file path starts with ./fixtures/
    if not filename.startswith('./fixtures/'):
        raise NameError(f"file name '{filename}' must come from /fixtures")
    
    # check that filename is in the format ./fixtures/<name>.csv
    parts = filename.split(".")
    if len(parts) != 3 or parts[1] == "" or parts[-1] != "csv":
       raise NameError(f"file name '{filename}' is not in the correct format")

    # check that filename is in /fixtures
    if filename not in filenames:    
        raise FileNotFoundError(f"file '{filename}' is not in /fixtures")

    # check that the file is not empty
    if os.stat(filename).st_size == 0:              
        raise ValueError(f"file '{filename}' is empty")
    
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
    for filename in sys.argv[1:]:                   
        check_filename(filename, filenames)             # check that filename is legal
        
    # convert all csv files to dataframes
    dataframes = []                                     # list of csv files converted to dataframes
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