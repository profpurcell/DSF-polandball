# It is probably possible to do this better, but this at least seems to work reasonably well

import pandas as pd
import requests
# Open up the file we will be working with (as a dataframe)
df = pd.read_csv("./data/2012 data/submissionList2012.csv")

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
            with open("./test-images/" + row['sub_id'] + ".jpg", "wb") as f:
                f.write(resp.content)
            checkList.append(name)
        else:
            otherList.append(row['url'])

df.apply(applyFunc, axis=1)

# now let's check for corrupted files
# code based on https://opensource.com/article/17/2/python-tricks-artists
from PIL import Image

corruptedList = []

for item in checkList:
    try:
        # try opening the file
        img = Image.open("./test-images/" + item)
        img.verify()
    except (IOError, SyntaxError) as e:
        # error - corrupted image
        corruptedList.append(item)

# If running this as a normal python file (not in Jupyter Notebook), make sure to save or print otherList and corruptedList