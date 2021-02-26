# Option for all at once?

import pandas as pd
import requests
from PIL import Image

# Open up the file we will be working with (as a dataframe)
df = pd.read_csv("./data/2012 data/submissionList2012.csv")

otherList = [] # submission urls that were not deleted, did not have an extension, and were not from imgur
# checkList = [] # file names of images we downloaded (to check)
corruptedList = [] # images that were corrupted
newList = [] # images that were downloaded and were not corrupted

# function to apply - will find all images that are missing an extension and try downloading them
def applyFunc(row):
    extension = row['url'].split(".")[-1]
    if ((row['text'] != ("[deleted]")) and (len(extension) != 3)):
        # if url includes imgur, try getting the jpg
        if ("imgur.com" in row['url']):
            url = row['url'] + ".jpg"
            # name = url.split("/")[-1]
            name = row['sub_id']
            resp = requests.get(url)
            with open("./test-images/" + name + ".jpg", "wb") as f:
                f.write(resp.content)
            # check
            try:
                img = Image.open("./test-images/" + name + ".jpg")
                img.verify()
                newList.append(name)
                return "jpg"
            except (IOError, SyntaxError) as e:
                corruptedList.append(name)
                # could possibly add code to remove file?
                return
        else:
            otherList.append(row['url'])
            return
    else: # add statement to make note of extension
        return extension

df['extension'] = df.apply(applyFunc, axis=1)

# print
print("Other List:")
for (item in otherList): print(item)
print("-"*60)
print("Corrupted List:")
for (item in corruptedList): print(item)
print("-"*60)
print("New List:")
for item in (newList): print(item)
