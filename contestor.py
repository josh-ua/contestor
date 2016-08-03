


#Imports - config has auth keys and userinfo
from datetime import datetime
import tweepy, time, config




#Imported from config.py (hidden from git)
#auth stuff
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
		print ("Searching and tweeting for term: " + searchTerm)
		for tweet in list:
			if tweet.in_reply_to_screen_name == None and hasRetweet(tweet) == True:
				try:
					api.retweet(tweet.id)
					likeThis(tweet)
					shouldFollow(tweet)
					tweetedCount = tweetedCount + 1
					time.sleep(5)
				except:
					notTweetedCount = notTweetedCount + 1
					continue
					
	print (str(tweetedCount) + " tweets SUCESSFULLY tweeted.")
	print (str(notTweetedCount) + " tweets NOT tweeted.")
	
	

#Checks if author should be followed (tweet contains following, follow, etc)	
def shouldFollow(tweet):
	followList = ["follow"]
	tweetText = (tweet.text).lower() #'follow' should account for all variations of the world (e.g. 'following') as well..
	
	for term in followList:
		if term in tweetText:
			if (hasattr(tweet,'retweeted_status') == True): ##if a retweet, follow original tweeter
				follow(tweet.retweeted_status.author.id)
			else:
				follow(tweet.author.screen_name)
			
			checkForExtraFollows(tweet)
			return;
			
		else:
			continue
			
			
#Checks if the tweet has "retweet" or "RT" in it. Otherwise it's probably not a contest tweet.
def hasRetweet(tweet):
	retweetList = ["retweet", "rt"]
	tweetText = (tweet.text).lower()
	
	for term in retweetList:
		if term in tweetText:
			return True
		else:
			continue
	
	return False
		
#Checks to see if the text in the tweet has the terms "like", "favorite", or "favourite" (for my British tweeters). 
#If so, the tweet will be favorited. Some giveaways require this.
def likeThis(tweet):
	likeList = ["like", "favorite", "favourite", "fav"]
	tweetText = (tweet.text).lower() ##lowercase so find function always works no matter the case (good work around ;))
	for term in likeList:
		if term in tweetText:
			api.create_favorite(tweet.id)
			return
		else:
			continue
			
			
			
#Some contents do a "retweet, follow me and @xxxx to win!" format. To account for this, this function parses the tweet.
#If another @[username] is found, they will be followed as well.
#TODO- punctuation needs to be stripped from handles
#e.g. if tweet reads: "Follow @xxxx!!" function will fail and throw expection
#also if tweet.author.screen_name == word, do not try to follow (optimize)
def checkForExtraFollows(tweet):
	try:
		words = tweet.text.split()
		for word in words:
				if word.find('@') == 0:
						follow(word.replace('@',""))
	except:  
		return;

		
		
#Randomly tweet things to seem more human(?) - still working on
#def clevTweet():
	#trends = api.trends_place(2514815)
	#data = trends[0]
	#trends = data['trends']
	#trendNames = [trend['name'] for trend in trends][0:5]

	#choice = random.choice(trendNames)
	#cbResponse = cb.ask(choice)
	#print (cbResponse + " " + choice)


	#if list size is zero, get new list of trends
	#randomly pick one, take it out of the list
	#ask cb, tweet response
				
				
				
#Follows user
def follow(authorID):
	try:
		api.create_friendship(authorID)
		maintainFollowing()
	except:
		return

	

#Maintains followers (twitter has some following/follower ratio limit). This keeps the following from going over 1000.
def maintainFollowing():
	friendslist = api.friends_ids(config.USERNAME)
	if  len(friendslist) > 1300:
		lastFollower = friendslist[len(friendslist) - 1]
		api.destroy_friendship(lastFollower)
		
		
#Runs function every 2 minutes.
while True :	
	main()
	print(str(datetime.now()))
	print("Sleeping for 300s...")
	time.sleep(300)
	print(" ")


			
		
	

	
###garbage:	
#	output.write(list[x].text.encode("utf-8"))










