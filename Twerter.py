#!/usr/bin/env python

from twython import Twython

APP_KEY = 'Consumer Key'
APP_SECRET = 'Consumer Secret'

OAUTH_TOKEN = 'Access Token'
OAUTH_TOKEN_SECRET = 'Access Token secret'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Test
twitter.verify_credentials()
twitter.update_status(status="Test Twerter post.")

# Post
post = raw_input("Write your tweet: ")
twitter.update_status(status=post)

# Get timelines
print twitter.get_user_timeline(screen_name = "name")
print twitter.get_home_timeline(count = 5)

# Search
print twitter.search(q="linux", result_type="popular")

# Follow
twitter.create_friendship(screen_name = "LinuxUserMag")

# Retweet
twitter.retweet(id = "12345")

# Favouriting
twitter.create_favorite(id = "12345")
print twitter.get_favorites()

# Mentions
print twitter.get_mentions_timeline(count="5")

# Trending
print twitter.get_place_trends(id="1")

# Retrieve lists
print twitter.get_list_statuses(id = "12345")
