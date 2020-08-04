# Reddit-PRAW-API
A simple scraper for the Reddit PRAW API

This script allows the user to scrape data from a given number of posts (up to 1,000) for a given subreddit.
The user will first need a Client ID, Client Secret, username, password, and user agent. These values should be manually inserted into the code. 

Once run, the script will give prompts asking for a subreddit and a number of posts. The subreddit should be entered without special characters (i.e. 'trees', not 'r/trees').
This script is designed to scrape the "hot" posts from the given subreddit (the most upvoted posts recently).

The script will output a .csv file with the name of the requested subreddt (e.g. 'trees.csv'). Each row in the .csv will contain this data for each post: 

title: the title of the post

author: the username of the poster

original content: whether the post has been marked as original content (boolean)

time created: the time (in UTC) the post was posted 

selfpost: whether the post has been marked as a selfpost (boolean)

stickied: whether the post is "stickied" to the top of the subreddit (boolean)

locked: whether the post has been locked by moderators (boolean)

NSFW: whether the post has been marked as containing adult content (boolean)

selftext: the body text of the post (if the post is a selfpost) 

number of comments: the number of comments on the post

score: the post's score (upvotes - downvotes) at the time of scraping

upvote ratio: the percentage of votes that have been upvotes

permalink: a direct link to the post

url: the link included in the post or a link to the post itself (if selfpost)

