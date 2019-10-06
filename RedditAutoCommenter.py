import praw
import time

reddit = praw.Reddit(client_id='f2Pcn3B31HsMuA',
                     client_secret='ImENvEwV0wjpJwPV72dwWZ3wIJo',
                     password='BananaApple',
                     user_agent='script:MusicFeedbackCommenter:v1.0 (by /u/MusicTest1234)',
                     username='MusicTest1234')

#print(reddit.user.me())

def searchSubreddit(subreddit):
    global postFound
    for submission in subreddit.new(limit=1):
        print('searching')
        if (submission.author == 'MusicTest1234') and (submission.title =="myTest"):
             postFound = True
             print(submission.title)
             print(submission.author)
        time.sleep(5)
   
        
subreddit = reddit.subreddit('test')
postFound = False

while (not postFound):
    searchSubreddit(subreddit)