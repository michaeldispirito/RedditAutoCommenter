import praw
import time
import datetime


targetSubreddit = 'test'
commentToPost = 'Test Comment'
authorOfPost = 'MusicTest1234'
titleOfPost = 'test number 10'
user = 'user'

daysAhead = 1
delay = 0

def createComment(post, time):
    post.reply(commentToPost)
    print('Comment Successfully Created at {}:{}:{}'.format(time.hour, time.minute, time.second))

def searchSubreddit(subreddit):
    global postFound
    searchTime = datetime.datetime.now()
    print('Searching at {}:{}:{}'.format(searchTime.hour, searchTime.minute, searchTime.second))
    for submission in subreddit.new(limit=10):
        if (submission.author == authorOfPost) and (submission.title == titleOfPost):
             postFound = True
             createComment(submission, searchTime)
             break
    time.sleep(2)
        
def getTimeToSearch():
    global delay
    global daysAhead
    curTime = datetime.datetime.now()

    if (curTime.weekday == 0 or curTime.weekday == 4):
        daysAhead = 0
    
    targetTime = datetime.datetime.today() + datetime.timedelta(days = daysAhead)
    targetTime = targetTime.replace(hour = 3, minute = 0, second = 0, microsecond = 0)
    
    delay = targetTime - curTime
    delay = delay.total_seconds()

#Connect to Reddit
reddit = praw.Reddit(client_id='abcdef',
                     client_secret='secret',
                     password='pass',
                     user_agent='script:WATMMFeedbackCommenter:v1.0 (by /u/user)',
                     username= user)

#Check if connection is made
if (reddit.user.me() == user):
    print('Connected to Reddit')

#Search the subreddit
subredditToSearch = reddit.subreddit(targetSubreddit)
postFound = False

getTimeToSearch()
print('Time until 3am in seconds = {}'.format(delay))

#time.sleep(30)

while (not postFound):
    searchSubreddit(subredditToSearch)