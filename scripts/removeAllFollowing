import tweepy, time, config


CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = 	config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_SECRET


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def unfollow():
	print()
	print("Unfollowing all users followed by: " + config.USERNAME)
	friendslist = api.friends_ids(config.USERNAME)
	friendsStart = len(friendslist)
	print("Currently following:" + str(friendsStart))
	for friend in friendslist:
		api.destroy_friendship(friend)
	if len(api.friends_ids(config.USERNAME)) == 0:
		print ("No more followers")
	else:
		print ("Failed to unfollow: " + str((friendsStart - (api.friends_ids(config.USERNAME)))))


###begin		
print("This script removes all friendships on the authed user ("+config.USERNAME+").")
while 0 == 0:
	answer = input("Do you want to do this? (y/n): ")
	if answer == "y":
		unfollow()
		break
	elif answer == "n":
		break

