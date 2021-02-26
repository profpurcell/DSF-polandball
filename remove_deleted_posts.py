# Remove deleted posts: 

# 2/23/21: 
# Got it to work

import pandas as pd

df1 = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/submissionList2012.csv")


# Create dataframe with  "text" != "[deleted]"

df_cleaned = df1[df1['text']!= "[deleted]"]

# Create dataframe with "text" == "[deleted]"

df_deleted = df1[df1['text'] == "[deleted]"]

#print(df_deleted[:10])


# The following code puts all entries with "text" = NaN into their own dataframe
    # Think it might be helpful in future, so I'm putting it here

null_columns = df_cleaned.columns[df_cleaned.isnull().any()]

df_null_text = df_cleaned[df_cleaned['text'].isnull()][null_columns]

#print(df_null_text[:10])


# Convert to csv

df_cleaned.to_csv("submissionList2012_cleaned.csv")

df_deleted.to_csv("submissionList2012_deleted.csv")
