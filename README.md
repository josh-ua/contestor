# contestor
contestor is a bot that enters twitter competitions. Built with python 3.5 and the Tweepy API. 

##what it does

contestor pulls the latest tweets with some fancy search terms geared towards giveaways. Then it retweets them and then follows the original tweeter. Also, if the world "like" or "favorite" or some variaiton is mentioned in the tweet, contestor will also like/favorite the tweet. The goal here is to enter as many twitter competitions as possible.

####features:
* an intense searching algorithm that decides what to tweet (a little bit of an overstatement)
* automatic retweet and follow for contest tweets (including tweets that say "also follow @xxxx")
* automatic like and favoriting for tweets that require it
* filters out tweets from "botspotters"
* keeps amount of followers <2000 to avoid follower limit (twitter has a ratio for this - apparantly if you have 0 following, you can only follow 2000 people)
* randomized resting times

##how to run it
Get the repo, fill out the sample config file with your twitter information, and run contestor.py. The scripts in the scripts directory are not needed to run, but may be useful to you. Their functions are self explanatory from their names. Tweepy is needed to use (pip install tweepy)

###to do:

others:
* tweet random things every once and a while (pull topics from trending topics - this is 80% done and uses cleverbot to comment on those topics)
* some type of stats tracked
* make contestor more customizable with a more advanced config.py
* play with timing for tweets - you can help by setting your own settings in the config.py

*(for more descriptive to do's, check the comments for each respective function in contestor.py)*


###stats:
Between testing, somewhere around 20,000 tweets have been rewteeted (so around that many contests have been entered) and *16* contests have been won. Please see the thingswon.md for a list of things won. Also, one account has been limited (following disabled...).
