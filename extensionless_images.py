 # Carson Comments:
    # Definitely found and downloaded more comics
    # It saved exactly 69 more comics
    # But I'm pretty sure there's over 100 w/o extensions in this year?
    # Good thing we got a list for that
    # Wait a sec
    # How do I save/print otherList and checkList?
    # VSCode says otherList and checkList are not defined
 
 # It is probably possible to do this better, but this at least seems to work reasonably well

import pandas as pd
import requests
# Open up the file we will be working with (as a dataframe)
# ./data/2012 data/submissionList2012.csv
df = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/submissionList2012.csv")

# submission urls that were not deleted, did not have an extension, and were not from imgur
otherList = []
# file names of images we downloaded (to check)
checkList = []

# function to apply - will find all images that are missing an extension and try downloading them
def applyFunc(row):
    if ((row['text'] != ("[deleted]")) and (len(row['url'].split(".")[-1]) != 3)):
        # if url includes imgur, try getting the jpg
        if ("imgur.com" in row['url']):
            url = row['url'] + ".jpg"
            name = url.split("/")[-1]
            resp = requests.get(url)
            # Rename the folder name
            with open("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/raw_comics2012_v2/" + row['sub_id'] + ".jpg", "wb") as f:
                f.write(resp.content)
            checkList.append(name)
        else:
            otherList.append(row['url'])

df.apply(applyFunc, axis=1)

# print(otherList[:10]) 

# I haven't checked for corrupted files yet
# now let's check for corrupted files
# code based on https://opensource.com/article/17/2/python-tricks-artists
