import pandas
import requests
from time import gmtime, strftime
import praw
from praw.models import MoreComments
from psaw import PushshiftAPI
import datetime as dt

def main():
    # set up connection
    reddit = praw.Reddit(client_id="",
        client_secret="",
        user_agent="")
    
    api = PushshiftAPI(reddit)
    start = int(dt.datetime(2020,10,2).timestamp())
    end = int(dt.datetime(2020,1,1).timestamp())

    # set up variables
    commentList = []
    submissionList = []
    awardList = []

    # loop through submissions
    
    # REMEMBER: Make an empty "raw_comics" folder before running
    for submission in api.search_submissions(before=start, after=end, subreddit="polandball", limit=10):
        submissionList.append(getSubmissionData(submission))
        # comments
        submission.comments.replace_more(limit=None)
        #print(len(submission.comments))
        for comment in submission.comments:
            #commentList.append(getCommentData(comment))  ##Gets comment data without finding child_comments
            commentList.extend(loopComment(comment, []))
        # submission awards
        if (submission.total_awards_received > 0): awardList.extend(getAwardData(submission))
        # comment awards
        for comment in submission.comments.list():
            if (comment.total_awards_received > 0): awardList.extend(getAwardData(comment))
            
    df1 =pandas.DataFrame(submissionList) 
    df1.to_csv("submissionList.csv")
    df2 =pandas.DataFrame(commentList) 
    df2.to_csv("commentList.csv")
    df3 = pandas.DataFrame(awardList)
    df3.to_csv("awardList.csv")

def getSubmissionData(submission):
    record = { #title of each column in our xlsx file
        "scraped_dat": strftime("%m/%d/%Y %H:%M:%S", gmtime()), #ATTENTION: Need to decide how to save time and date
        "sub_id": submission.id,
        "sub_fullname": submission.name,
        "author": submission.author,
        "title": submission.title,
        "gmt_time": strftime("%m/%d/%Y %H:%M:%S", gmtime(submission.created_utc)),
        "unix_time": submission.created_utc,
        "num_comments": submission.num_comments,
        "upvotes": submission.score,
        "ratio": submission.upvote_ratio,
        "is_self": submission.is_self,
        "is_stickied": submission.stickied,
        "is_OC": submission.is_original_content,
        "distinguished": submission.distinguished,
        "url": submission.url,
        "text": submission.selftext
    }
    saveImage(submission)
    
    record = getAuthorPremium(submission, record)
    record = getAuthorFlair(submission, record)
    record = getAwards(submission, record)
    
    return record
    
def saveImage(submission):
    if (submission.selftext != "[deleted]") and (submission.url.split(".")[-1] in ["png", "jpg", "gif", "tif", "bmp"]):
        image_extension = submission.url.split(".")[-1]
        resp = requests.get(submission.url)
        with open("raw_comics/" + submission.id + "." + image_extension, "wb") as f:
            f.write(resp.content)

def getCommentData(comment):
    record = {
        "scraped_dat": strftime("%m/%d/%Y %H:%M:%S", gmtime()),
        "gmt_time": strftime("%m/%d/%Y %H:%M:%S", gmtime(comment.created_utc)),
        "unix_time": comment.created_utc,
        "sub_id": comment.submission,
        "sub_fullname": comment.link_id,
        "parent_id": comment.parent_id,
        "com_fullname": comment.fullname,
        "com_id": comment.id,
        "commenter": comment.author,
        #"flair_id": comment.author_flair_css_class, # won't let me use richtext indicces for some reason
        "depth": comment.depth,
        "is_root": comment.is_root,
        "is_op": comment.is_submitter,
        "is_stickied": comment.stickied,
        "distinguished": comment.distinguished,
        "is_controversial": comment.controversiality,
        "is_edited": comment.edited,
        "upvotes": comment.score,
        "gold": comment.gilded,
        "url": comment.permalink,
        "body": comment.body
    }
    
    record = getAuthorPremium(comment, record)  
    record = getAuthorFlair(comment, record)    
    record = getAwards(comment, record)
    
    return record

def getAuthorFlair(item, d):     
    try:
        d["author_flair_name"] = item.author_flair_richtext[0]['a'] # the name of the emoji
        d["author_flair_text"] = item.author_flair_richtext[-1]['t'].strip() # the text that goes with the flair
        d["author_flair_url"] = item.author_flair_richtext[0]['u'] # the url for the flair
        d["author_hussar"] = (len(item.author_flair_richtext) > 2)
    except:
        d["author_flair_name"] = ""
        d["author_flair_text"] = ""
        d["author_flair_url"] = ""
        d["author_hussar"] = False
    return d

def getAuthorPremium(item, d):
    try:
        d["author_premium"] = item.author_premium
    except:
        d["author_premium"] = ""
    return d

def getAwards(item, d):
    # total number received
    d["total_awards"] = item.total_awards_received
    # value of all awards
    value = 0
    for award in item.all_awardings:
        value = value + (award['count']*award['coin_price'])
    d["total_award_value"] = value
    return d

def getAwardData(item):
    awardList = []
    for award in item.all_awardings:
        record = {
            "item_fullname": item.fullname,
            "award_name": award['name'],
            "award_count": award['count'],
            "award_price": award['coin_price']
        }
        awardList.append(record)
    return awardList

def loopComment(comment, commentList):
    x = 0 # for counting all child comments
    d = {} # set up empty dictionary
    d = getCommentData(comment)
    # loop through replies
    for reply in comment.replies:
        commentList.extend (loopComment(reply, [])) # add data from the reply to list
        x = x + 1 + commentList[-1]['child_comments']
    d['child_comments'] = x
    commentList.append(d)
    return(commentList) #as soon as you include a return statement, a function or loop ends
    #return limitation - can only return one thing

main()