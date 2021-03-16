# Create clean dataset and corresponding dropped dataset: 

import pandas as pd

# Note:
    # not working for commentList2013
    # Error:
        # pandas.errors.ParserError: Error tokenizing data. C error: Buffer overflow caught - possible malformed input file.
    # Also, everything after 2013 has thrown this warning for me:
        # sys:1: DtypeWarning: Columns (3) have mixed types. Specify dtype option on import or set low_memory=False.

# REMEMBER:
    # Change the file path within pd.read_csv to whatever file you want to clean
    # Then change each function's arguments to correspond to the file before you run
df1 = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/2015/commentList2015.csv")

# The following code:
 # Creates three functions: createCleanedDataset, createDroppedDataset, and createNullDataset
 # Each of these functions includes the same four parameters:
    # df
        # accepts dataframes, in our case d1
    # col
        # accepts a string = the name of the column that you want to clean
        # for submissionList: col = 'text'
        # for commentList: col = 'body'
    # data
        # accepts a string that indicates the type of data: "submission" vs. "comment"
        # used to name the csv file
    # year
        # accepts a string that indicates the year: "2011", "2012", etc.
        # used to name the csv file
# Only two functions are called in this program: createCleanedDataset, createDroppedDataset
    # I included the createNullDataset function in case we wanted to use it later
# Go to the bottom of this code to adjust the arguments for data and year before running it

# Create csv without "[deleted]" and "[removed]" posts
def createCleanedDataset(df, col, data, year):
    df_deleted = df[df[col] != "[deleted]"]
    df_cleaned = df_deleted[df_deleted[col] != "[removed]"]
    df_cleaned.to_csv(data + "List" + year + "_cleaned.csv")


# Create csv with only "[deleted]" and "[removed]" posts
def createDroppedDataset(df, col, data, year):
    df_deleted = df[df[col] == "[deleted]"]
    df_removed = df[df[col] == "[removed]"]
    # combine df_deleted and df_removed into one dataframe:
    dropped = [df_deleted, df_removed]
    # concat adds df_removed to the bottom of df_deleted
    df_dropped = pd.concat(dropped) 
    df_dropped.to_csv(data + "List" + year + "_dropped.csv")


# The following code puts all entries with "text" = NaN into their own dataframe
    # Think it might be helpful in future, so I'm putting it here
def createNullDataset(df, col, data, year):
    null_columns = df.columns[df.isnull().any()]
    df_null_text = df[df[col].isnull()][null_columns]
    df_null_text.to_csv(data + "List" + year + "_nullText.csv")

# REMEMBER:
    # Change year argument 
    # Change data argument from "submission" to "comment" if you're cleaning the commentList
createCleanedDataset(df1, 'body', "comment", "2015")
createDroppedDataset(df1, 'body', "comment", "2015")



# Note: I'm pretty sure everything is out of order in df_cleaned and df_dropped
# That can be easily fixed in both Python or Excel, it's just something to remember for later
