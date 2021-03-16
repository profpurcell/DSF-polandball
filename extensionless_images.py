<<<<<<< HEAD
<<<<<<< HEAD
 # start: 466 items
 # end: 535 items
=======
 # Carson Comments:
    # Definitely found and downloaded more comics
    # It saved exactly 69 more comics
    # But I'm pretty sure there's over 100 w/o extensions in this year?
    # Good thing we got a list for that
    # Wait a sec
    # How do I save/print otherList and checkList?
    # VSCode says otherList and checkList are not defined
 
 # It is probably possible to do this better, but this at least seems to work reasonably well
>>>>>>> 4069414091ad92d39249ad07ea96bee84eafe06a
=======
 # start: 466 items
 # end: 535 items
>>>>>>> 1284fd2469800b8aa2b7da7606dccb85ab66a40c

import pandas as pd
import requests
from PIL import Image
from pandas import DataFrame
# Open up the file we will be working with (as a dataframe)
# ./data/2012 data/submissionList2012.csv
df = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/2012/submissionList2012_cleaned.csv")

# submission urls that were not deleted, did not have an extension, and were not from imgur
otherList = []
# file names of images we downloaded (to check)
#checkList = []
corruptedList = []
newList = []

def applyFunc(row):
    extension = row['url'].split(".")[-1]
    if ((row['text'] != ("[deleted]")) and (len(extension) != 3)):
        # if url includes imgur, try getting the jpg
        if ("imgur.com" in row['url']):
            url = row['url'] + ".jpg"
            # name = url.split("/")[-1]
            name = row['sub_id']
            resp = requests.get(url)
            with open("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/2012/raw_comics2012/" + name + ".jpg", "wb") as f:
                f.write(resp.content)
            # check
            try:
                img = Image.open("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/2012/raw_comics2012/" + name + ".jpg")
                img.verify()
                newList.append(name)
                return "jpg"
            except (IOError, SyntaxError) as e:
                corruptedList.append(name)
                # will look at corruptedFiles.csv to see if we need to remove images
                return
        else:
            otherList.append(row['url'])
            return
    else: # add statement to make note of extension
        return extension

df.apply(applyFunc, axis=1)


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1284fd2469800b8aa2b7da7606dccb85ab66a40c
df_otherList = DataFrame(otherList, columns = ["url"])
df_otherList.to_csv("otherList2012.csv")

df_newList = DataFrame(newList, columns = ["name"])
df_newList.to_csv("newList2012.csv")

df_corruptedList = DataFrame(corruptedList, columns = ["name"])
df_corruptedList.to_csv("corruptedList2012.csv")

# If running this as a normal python file (not in Jupyter Notebook), make sure to save or print otherList and corruptedList
<<<<<<< HEAD
=======
# I haven't checked for corrupted files yet
# now let's check for corrupted files
# code based on https://opensource.com/article/17/2/python-tricks-artists
>>>>>>> 4069414091ad92d39249ad07ea96bee84eafe06a
=======
>>>>>>> 1284fd2469800b8aa2b7da7606dccb85ab66a40c
