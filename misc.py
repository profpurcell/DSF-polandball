# Use apply with tesseract to get text from comics

import pandas as pd

df = pd.read_csv("path_to_file.csv")

# function to apply
def applyFunc(row):
    name = row["id"]
    extension = row["url"].split(".")[-1]
    # make sure we actually have something
    if not (extension in ["png", "jpg", "gif", "tif", "bmp"]):
        return
    filename = "filepath" + name + "." + extension
    text = "apply tesseract here"
    return text

# apply
df["text"] = df.apply(applyFunc, axis=1)

# TODO: Save the DataFrame

#########################################################################
#########################################################################
#########################################################################

# Remove deleted posts
import pandas as pd

data = [
    {"a": 1, "b": "x", "content": "some content"},
    {"a": 2, "b": "x", "content": "[deleted]"},
    {"a": 3, "b": "y", "content": "[deleted]"},
    {"a": 4, "b": "y", "content": "some content"}
]
df = pd.DataFrame(data)

df2 = df[df.content != "[deleted]"]

df_deleted = df[df.content == "[deleted]"]

# If you want to remove the comments, make sure to save the deleted submissions in their own csv