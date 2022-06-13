import tweepy

import tweepy
auth = tweepy.OAuthHandler('j8dNsOA2DEKXrD5vcgelWIhjC', 'VJLkZguqSoCnwdE2pblF0DmvrNLFNDbdlbqsFnDyRmaKDYRIWz')
auth.set_access_token('1027693267708723201-c5yPLNknTRGy9PeQ74ItkwHy8Py72R', 'krirakXTS3jK0cm68QzLrnFNAgDTDDIuOpXoOPZfodtcz')

api = tweepy.API(auth)

# screen_name = '@ArekeAyomide4'
# user = api.get_user(screen_name= '@ArekeAyomide4')

#def limit_handle(cursor):
    #try:

       # while True:
           # yield cursor.next()
    #except tweepy.R
#generous Bot

# for follower in tweepy.Cursor(api.get_followers).items() :
#     if follower.name == 'O P E Y E M I':
#         follower.follow()
#     #print(follower.screen_name)


search_string = '#ASUU'
numberOfTweets = 10
for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numberOfTweets):
    try:
        tweet.retweet()
        print('I liked that tweet')
    except AttributeError as e:
        print(e)
