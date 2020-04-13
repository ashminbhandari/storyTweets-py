# Listens for Tweets

#Exit
import sys

# Config import, put all your secrets here
from config import config

# Twitter API
import twitter

# Import take screenshot function from twitterBot
from twitterBot import takeScreenshot

# Instagram bot to post to instagram stories
from instagramBot import postToStory, instagramSetup

# Import time to sleep
import time

#Set up and save user data for Instagram to avoid future logins.
instagramSetup()

# Setting up the twitter API
api = twitter.Api(consumer_key=config['consumer_key'],
                  consumer_secret=config['consumer_secret'],
                  access_token_key=config['access_token_key'],
                  access_token_secret=config['access_token_secret'])

# Check if all keys and secrets are correct
api.VerifyCredentials()

# Twitter screen name
screenName = config['screen_name']

#Get current status
status = api.GetUserTimeline(screen_name=screenName, count=1)

#Listen for tweets
while 1:
    print('Listening for tweets...')
    latestStatus = api.GetUserTimeline(screen_name=screenName, count=1)

    if latestStatus[0].text != status[0].text:
        print('Heard new tweet...')
        tweetURL = 'https://twitter.com/' + screenName + '/status/' + latestStatus[0].id_str
        if takeScreenshot(tweetURL):
            if postToStory():
                status = latestStatus

    time.sleep(config['listening_freq'])