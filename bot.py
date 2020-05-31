# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:57:59 2020

@author: jmanu
"""

import tweepy
from credentials import *


def twitter_setup():
    #https://developer.twitter.com/en/apps
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


if __name__ == '__main__':    
    # Get access and key from another class
    bot = twitter_setup()

    try:
        bot.update_status("Probando mi robot antes de inicar ponencia xD")
        print("Done")
    except tweepy.TweepError as e:
        print(e.reason)
