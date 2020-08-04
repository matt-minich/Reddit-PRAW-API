import praw
import csv
from datetime import datetime

reddit = praw.Reddit(client_id = 'Client_ID', client_secret='Client_secret',
                     username='Username' , password = 'Password', user_agent ='User Agent' )


term = input('Which subreddit would you like to scrape? ')
limit = int(input('How many posts would you like to scrape? '))
subterm = reddit.subreddit(term)

subreddit = subterm.hot(limit=limit)
#

with open('%s.csv' %term,'w', encoding = 'utf-8') as csvfile:
    fieldnames = ['title','author','original content','selfpost','time created','stickied','locked','NSFW','selftext','number of comments','score','upvote ratio','permalink','url']
    filewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
    filewriter.writeheader()

    for i in subreddit:

        ts = datetime.utcfromtimestamp(i.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        filewriter.writerow({'title':i.title,
                            'author':i.author,
                            'original content':i.is_original_content,
                            'selfpost':i.is_self,
                            'time created':ts,
                            'stickied':i.stickied,
                            'locked':i.locked,
                            'NSFW':i.over_18,
                            'selftext':i.selftext,
                            'number of comments':i.num_comments,
                            'score':i.score,
                            'upvote ratio':i.upvote_ratio,
                            'permalink':i.permalink,                
                            'url':i.url})

print ('We did it!')
