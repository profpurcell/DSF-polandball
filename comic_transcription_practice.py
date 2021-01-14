# README
## you'll need to change the file path of "files = glob.glob()" if you want to mess with this yourself
## also need to specify the file path of "pytesseract.pytesseract.tesseract_cmd = " to where tesseract is

import pandas
import glob
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'c:\program files\Tesseract-OCR\tesseract.exe'


def getTranscript():
    textList = []
    # Get all .png file names in a folder with glob:
    files = glob.glob('/Users/carson/OneDrive - University of Oklahoma/Desktop/DSF Data/comic_files/*.png',
    # * indicates all files that end in .png
    # so could run into a problem if the image is saved as .gif or .jpg
                 recursive = True)
    # Use tesseract to transcribe the comic, save file name and transcript to a dictionary
    # Is there a way to isolate the comic id from the file name? 
    for file in files:
        img = cv2.imread(file)
        text = pytesseract.image_to_string(img)
        record = {
            "file": file,
            "transcription": text
        }
        textList.append(record)
    #return record
    
    df = pandas.DataFrame(textList)
    df.to_csv("practiceTranscriptions.csv")


getTranscript()

# Note:
    # I tested this on a sample of 30 polandball comics 
    # It took 1 minute to run
    # Is there a way to make it faster?
    # I know Tyler said to use apply() but I wasn't sure how to incorporate it