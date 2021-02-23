# 2/18/21 Carson Comments:
    # Added code to skip [deleted] files
    # That helped 
    # It still threw an error when it ran into a Wikimedia png
    # Error:
        # pytesseract.pytesseract.TesseractError: (1, 'Tesseract Open Source OCR Engine v5.0.0-alpha.20200328 with Leptonica Error in fopenReadStream: file not found Error in 
        # pixRead: image file not found: File not found: /v1/AUTH_mw/wikipedia-commons-local-public.6a/6/6a/Britain_knows_everything_better_again.png 
        # Image file File not found: /v1/AUTH_mw/wikipedia-commons-local-public.6a/6/6a/Britain_knows_everything_better_again.png cannot be read! 
        # Error during processing.', 'occurred at index 301') 
    
    # Maybe this calls for more cleaning?
    # Ooo might've been useful to generate a kind of "image receipt" column whenever we correctly downloaded an image
        # and saved it to a folder

    # TODO:
        # Create a submissionList2012_delete_cleaned
        # Run this program on that cleaned file
        # Figure out how best to incorporate the extensionless images into all of this

# Use apply with tesseract to get text from comics

import pandas as pd
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'c:/program files/Tesseract-OCR/tesseract.exe'

df = pd.read_csv("C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/COPY_submissionList2012.csv")

textSubmissionList = []

# function to apply
def applyFunc(row):
    name = row["sub_id"]
    if (row['text'] != ("[deleted]")):
        extension = row["url"].split(".")[-1]
        # make sure we actually have something
        if not (extension in ["png", "jpg", "gif", "tif", "bmp"]): # I don't think tesseract can process gif and bmp
            return
        filename = "C:/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Datasets/raw_comics2012/" + name + "." + extension
        text = pytesseract.image_to_string(filename)
        return text

# apply
df["image_text"] = df.apply(applyFunc, axis=1)

# TODO: Save the DataFrame

#########################################################################
#########################################################################
#########################################################################
