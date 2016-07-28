#Imports - config has auth keys and userinfo
import tweepy,  config

#Imported from config.py (hidden from git)
#auth stuff
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = 	config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#####################################################################
#This script deletes all direct messages the auth user has recieved.#
#####################################################################

directMessages = api.direct_messages()
##Grabs list of DM's

if (len(directMessages) = 0): ##check to see if there are any
    print 'You have no direct messages to delete!'
else: ##cycles through and deletes them
    while (len(directMessages)) > 0:
        for message in directMessages:
            api.destroy_direct_message(message.id)
        directMessages = api.direct_messages()


print ('Done. All your DMs should be gone.')
