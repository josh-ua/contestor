

#Imports - config has auth keys and userinfo
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


searchList = ["rt to win", "retweet giveaway", "retweet win"]

def main():
	tweetedCount = 0
	notTweetedCount = 0
	for searchTerm in searchList:
		list = api.search(q=searchTerm, rpp = 50)
		for tweet in list:
			if tweet.in_reply_to_screen_name == None:
				try:
					api.retweet(tweet.id)
					likeThis(tweet)
					tweetedCount = tweetedCount + 1
					
					if (hasattr(tweet,'retweeted_status') == True): ##if a retweet, follow original tweeter
						follow(tweet.retweeted_status.author.id)
					else:
						follow(tweet.author.screen_name)
				except:
					notTweetedCount = notTweetedCount + 1
					continue
					
	print (str(tweetedCount) + " tweets tweeted.")
	print (str(notTweetedCount) + " tweets NOT tweeted.")
	
	
#Checks to see if the text in the tweet has the terms "like", "favorite", or "favourite" (for my British tweeters). 
#If so, the tweet will be favorited. Some giveaways require this.
def likeThis(tweet):
	likeList = ["like", "favorite", "favourite", "fav"]
	tweetText = (tweet.text).lower() ##lowercase so find function always works no matter the case (good work around ;))
	for term in likeList:
		if term in tweetText:
			api.create_favorite(tweet.id)
		else:
			continue
	





#Some contents do a "retweet, follow me and @xxxx to win!" format. To account for this, this function parses the tweet.
#If another @[username] is found, they will be followed as well.
#TODO--

#def checkForFollow(tweet):
#
#words = tweet.text.split()
#
#toFollow = []
#for word in words:
#        if word.find('@') == 0:
#                toFollow.append(word)


                

	
	
	
#Follows user
def follow(authorID):
	try:
		api.create_friendship(authorID)
		maintainFollowing()
	except:
		return ##already followed 
	

#Maintains followers (twitter has some following/follower ratio limit). This keeps the following from going over 1000.
def maintainFollowing():

	friendslist = api.friends_ids(config.USERNAME)
	if  len(friendslist) > 1999:
		lastFollower = friendslist[len(friendslist) - 1]
		api.destroy_friendship(lastFollower)

		


while True :	
	main()
	print(str(datetime.now()))
	print("Sleeping for 180s...")
	time.sleep(180)
	print(" ")


			
		
	

	
	

	
###garbage:	
#	output.write(list[x].text.encode("utf-8"))










