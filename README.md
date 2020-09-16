# DSF-polandball
DSF - Polandball Project

## Collection Notes

- collecting after one week should be best
- make note of meta/announcement posts

### Data to Collect

- image
- submission date
- author/submitter
- post title
- upvotes/downvotes
- tags
- number of comments
- post id
- comments
	- comment id
	- poster
	- text
	- parent comment (comment or post id)

### Data Structure

Top level folder
	images/
		- images, named with post id
	posts.csv
		- post id, post title, author, author flair, submission date, upvotes/downvotes, tags (??), date of scraping, image filename
	comments.csv
		- comment id, parent id (comment or post id), comment level, author, author flair, text, comment date, date of scraping
