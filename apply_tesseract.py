# 2/18/21 Carson Comments:

# did not transcribe any comics to image_text

# TODO:
# Add a 'image_text' col and save text there

# TODO:
    # Dataset cleaning process:
    # if Tesseract reports an error
        # 1. Write down the index where it occurred
        # 2. Find the submission id
        # 3. Manually check the image in raw_comics
        # 4. Remove image if it is not relevant

# Use apply with tesseract to get text from comics

import pandas as pd
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'c:/program files/Tesseract-OCR/tesseract.exe'

df1 = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/2012/submissionList2012_cleaned.csv")

textSubmissionList = []

#df_small = df[290:310]

# function to apply
def applyFunc(row):
    name = row["sub_id"]
    if (row['text'] != ("[deleted]")):
        extension = row["url"].split(".")[-1] # TODO change to new extesnion column
        # make sure we actually have something
        if not (extension in ["png", "jpg", "gif", "tif", "bmp"]): # I don't think tesseract can process gif and bmp
            return
        try:
            filename = "C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/raw_comics2012/" + name + "." + extension
            text = pytesseract.image_to_string(filename)
            return text
        except:
            return

# remove tvwpb.png <-- not a real image

# apply
df1["image_text"] = df1.apply(applyFunc, axis=1)

df1.to_csv("TESSAsubmissionList2012_cleaned.csv")

#print(df1[:10])

# TODO: Save the DataFrame

#########################################################################
#########################################################################
#########################################################################
