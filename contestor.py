

#Imports - config has auth keys
from datetime import datetime
import tweepy, time, config




#Imported from config.py (hidden from git)
CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = 	config.ACCESS_TOKEN
ACCESS_SECRET = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


def main():
	list = api.search(q="rt to win", rpp = 2)
	for tweet in list:
		if tweet.retweeted == False and tweet.in_reply_to_screen_name == None and checkTweetedAlready(tweet) == False:
			#api.retweet(tweet.id)
			print(tweet.author.screen_name)
			print(tweet.user.id)
			print(tweet.in_reply_to_user_id)
			print(hasattr(tweet,'retweeted_status'))
			print(tweet.retweeted_status)
			#api.create_friendship(tweet.user.id)
		
		
#See if this tweet was retweeted within the last 50 tweets
def checkTweetedAlready(checkTweet):
	tweetedAlready = False
	tweetList = api.user_timeline(count = 50, include_rts=True)
	for tweet in tweetList:
		if tweet.text == checkTweet.text:
			tweetedAlready = True
			break
	return tweetedAlready
		

	


#def follow(tweet):
#	isFollowing = False
#	friendslist = api.friends_ids(config.USERNAME)
#	for following in friendslist:  ##compares already following ideas with user id of who tweeted
#		if following == tweet.user.id:
	#		isFollowing = true
	#		break
			
	#if isFollowing == False:
	
	
	#maintainFollowing()

def maintainFollowing():
	#keeps followers under 1000 (twitter has a following limit)
	friendslist = api.friends_ids(config.USERNAME)
	if  len(friendslist) > 999:
		lastFollower = friendslist[len(friendslist) - 1]
		api.destroy_friendship(lastFollower)

		
#to do: implement run function

x = 0
while x < 2 :
	
	main()
	print(str(datetime.now()))
	print("Sleeping for 300s...")
	##
	print(" ")
	x = x +1

			
		
	

	
	

	
###garbage:	
#n = "\n"
#nb = str.encode(n)


#tweetIDs = [ ] 
#for x in range(0, len(list)-1):
#	output.write(list[x].text.encode("utf-8"))
#	output.write(nb)
#	tweetIDs.insert(0, list[x].id)
	









