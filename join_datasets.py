# 6/21/2021
# Join the DSF-polandball dataset with the polandball moderator dataset
# Using a left join

import pandas as pd

# Import the OU DSF-polandball submissions dataset
df1 = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/Cleaned Datasets/polandballSubmissions.csv")

# Deal with duplicates
print(len(df1.index))
# drop duplicates
df1 = df1.drop_duplicates(subset=['sub_id'])
print(len(df1.index))

# Import the r/polandball moderators' comic dataset
df2 = pd.read_excel("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/polandball_main.xlsx")

# Deal with duplicates
print(len(df2.index))
# drop duplicates
df2 = df2.drop_duplicates(subset=['id'])
print(len(df2.index))

# Drop variables in the polandball comic dataset that we already have in our dataset or are uninformative
df2 = df2.drop(columns = ['Date', 'Directlink', 'Timestamp', 'Title', 'User', '~'])

# We are going to join based on the submission id
# df1_key = "sub_id"
# df2_key = "id"

merged_left = pd.merge(left=df1, right=df2, how='left', left_on='sub_id', right_on='id')
print(len(merged_left.index))

# The following code is simply another way to do the above:
    #merged_left = df1.reset_index().merge(df2, how="left", left_on='sub_id', right_on='id').set_index('index')
    # Drop some extraneous index columns
    #merged_left = merged_left.drop(columns = ['id_x', 'index.1'])


# Note about similar columns:
    # num_comments and mod_comments appear to be the same
    # upvotes and mod_score appear to be the same
    # an inner join and comparison between the columns of interest revealed they are different at points
    # so which column is the preferred measure will be left to the user



# Rename columns to follow our naming conventions:
merged_left = merged_left.rename(columns={'Backup':'mod_is_backup', 'Comments':'mod_num_comments', 
 'Countries (Comment)':'mod_countries_comment', 'Countries (OCR)':'mod_countries_ocr', 'Flair (Post)':'mod_flair_post',
 'Flair (User)':'mod_author_flair', 'OCR Dialogue':'mod_ocr_dialogue', 'Permalink':'mod_permalink', 
 'Real Comments':'mod_real_num_comments', 'Score':'mod_score', 'Source':'mod_source', 'Status':'mod_status', 
 'URL (Backup)':'mod_backup_url', 'id_y':'mod_sub_id', 'scraped_dat':'scraped_time'})

print(sorted(merged_left))

# rename is successful

# Drop extraneous/incorrect index column:
merged_left = merged_left.drop(columns=['id_x'] )

# Check Data types
print(merged_left.dtypes)

#Convert gmt_time to datetime
merged_left['gmt_time']= pd.to_datetime(merged_left['gmt_time'])
print(merged_left.gmt_time.dtype)

merged_left['scraped_time']= pd.to_datetime(merged_left['scraped_time'])
print(merged_left.scraped_time.dtype)

# Note for unix_time:
    # Can use:
        # datetime_time = datetime.datetime.fromtimestamp(unix_time)
    # to convert unix time to datetime
    # Can format this by adding:
        # .strftime('%d-%m-%y')

#TODO
# What are Status and Source?

# FIXME
    # Currently end up with 3 index columns:
        # 'index' = the correct index for the combined datatset
        # 'index.1 = appears to be the exact same as 'index'
        # 'id_x' = appears to be completely empty
    # Conclusion: Remove 'index.1' and 'id_x' before converting to csv
    # Also of note:
        # 'id_y' = submission ids from the moderator dataset
        # Rename to 'mod_sub_id'

# Create final csv
merged_left.to_csv("FINALpolandballSubmissionsData.csv", index=False, encoding='utf-8-sig')
