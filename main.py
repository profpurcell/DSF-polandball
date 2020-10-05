# import statements
import praw

def main():
    # set up connection
    reddit = praw.Reddit(client_id="",
        client_secret="",
        user_agent="")

    # set up variables
    commentList = []
    submissionList = []
    awardList = []

    # loop through submissions
    # TODO: Determine what submissions to scrape
    for submission in reddit.subreddit("polandball").hot(limit=10):
        submissionList.append(getSubmissionData(submission))
        # comments
        submission.comments.replace_more(limit=None)
        for comment in submission.comments:
            commentList.extend(loopComment(comment, []))
    
    # TODO: write data to CSVs


# functions

# collect data from a submission
def getSubmissionData(submission):
    d = {} # set up empty dictionary
    # TODO: add submission data
    d['num_comments'] = len(submission.comments.list())
    # TODO: add image
    url = ""
    ## TODO: if image, update url
    d['image'] = url
    return d

# collect data from a comment
def getCommentData(comment):
    d = {} # set up empty dictionary
    # TODO: get date of collection
    # TODO: get date of comment (comment.created_utc)
    d["author"] = comment.author # the author of the comment
    d = getAuthorFlair(comment, d)
    d["body"] = comment.body # body of the comment
    d["depth"] = comment.depth # depth of comment - 0 for top level comment, 1 for next level, etc.
    d["id"] = comment.fullname # could also get id - fullname adds prefix tx_ to id where x=3 for a submission and 1 for a comment
    d["is_root"] = comment.is_root # somewhat redundant - depth = 0, but could be useful as a separate column
    d["is_submitter"] = comment.is_submitter # author id matches poster id
    d["submission_id"] = comment.link_id # could be useful for keeping things together
    d["parent_id"] = comment.parent_id # submission id for top level comment, comment id for lower level
    d["score"] = comment.score # number of upvotes
    d["total_awards"] = comment.total_awards_received

    # other data possibilities
    # author_premium
    # controversiality - probably not useful since downvotes seem to be primarily disabled
    # distinguished?
    # edited?
    # gilded or gildings?
    # locked?
    # stickied?

    return d

# get author flair (consistent for submission and comment)
# item - submission or comment, d - dictionary
def getAuthorFlair(item, d):
    # TODO: Decide what info to collect for author flair
    # This is actually somewhat complicated as the flair for honorary winged hussars is different
    #d["author_flair_name"] = item.author_flair_richtext[0]['a'] # the name of the emoji
    #d["author_flair_url"] = item.author_flair_richtext[0]['u'] # the url for the emoji
    d["author_flair_text"] = item.author_flair_richtext[-1]['t'].strip() # the text that goes with the flair
    return d

# get awards (consistent for submission and comment)
# item - submission or comment, d - dictionary
# TODO: Decide where to apply this
def getAwards(item, awardList):
    # TODO: Decide what to get from here
    for award in item.all_awardings:
        d = {} # new dictionary
        d["name"] = award['name']
        d["count"] = award['count']
        awardList.append(d)
    return awardList

# loop through a comment
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
    return commentList


# run

main()