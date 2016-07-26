# contestor
contestor is a bot that enters twitter competitions. Built with python 3.5 and the Tweepy API. 

##what it does

contestor pulls the latest tweets with some fancy search terms geared towards giveaways. Then it retweets them and then follows the original tweeter. Also, if the world "like" or "favorite" or some variaiton is mentioned in the tweet, contestor will also like/favorite the tweet. The goal here is to enter as many twitter competitions as possible.

####features:
* an intense searching algorithm that decides what to tweet (a little bit of an overstatement)
* automatic retweet and follow for contest tweets (including tweets that say "also follow @xxxx")
* automatic like and favoriting for tweets that require it
* keeps amount of followers <2000 to avoid follower limit (twitter has a ratio for this - apparantly if you have 0 following, you can only follow 2000 people)



##how to run it
Get the repo, fill out the sample config file with your twitter information, and run contestor.py. The scripts in the scripts directory are not needed to run, but may be useful to you.

###to do:
* tweet random things every once and a while (pull topics from trending topics)
* only tweet if the tweet has 'retweet' or 'RT' in it
* implement a "delete all DM's" script (or ones that have been marked as read)
* some type of stats tracked
* make contestor more customizable with a more advanced config.py
* improve checkForFollow function (need punctuation from handles to be stripped)
* play with timing for tweets - right now it's at **300s**

*(for more descriptive to do's, check the comments for each respective function in contestor.py)*


###stats:
Between testing, somewhere around 3,000 tweets have been rewteeted (so around that many contests have been entered) and nothing has been won yet. Also, one account has been limited (following disabled...)
