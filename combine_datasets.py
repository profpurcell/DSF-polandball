# 6/21/2021
# Combine the cleaned submission datasets
# Do not confuse with join_datasets.py, which merges our DSF-polandball submission data with the moderators' submission data

# FIXME: Check this warning
    # FutureWarning: Sorting because non-concatenation axis is not aligned. A future version of pandas will change to not sort by default.
        #To accept the future behavior, pass 'sort=False'.
        #To retain the current behavior and silence the warning, pass 'sort=True'.

# import packages
import os
import glob
import pandas as pd

# set working directory
os.chdir("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/Cleaned Datasets/Submissions")

# use glob to match file type extension
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine and export the new csv
combined_df = pd.concat([pd.read_csv(f) for f in all_filenames ]).reset_index(drop=True)

#export to csv
combined_df.to_csv( "polandballSubmissions.csv", index=True, encoding='utf-8-sig')