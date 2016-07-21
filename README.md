# contestor
contestor is a bot that enters twitter competitions. Built with python, he strives to be the very best. Still a work in progress, although the base functions do work.

##what it does

contestor pulls the latest tweets with some fancy search terms geared towards giveaways. Then it retweets them and then follows the original tweeter. Also, if the world "like" or "favorite" or some variaiton is mentioned in the tweet, contestor will also like/favorite the tweet. The goal here is to enter as many twitter competitions as possible.

##how to run it

Get the repo, fill out the sample config file with your twitter information, and run contestor.py. The scripts in the scripts directory are not needed to run, but may be useful to you.

###to do:
* tweet random things every once and a while (pull topics from trending topics)
* implement checkForMoreFollowing function
* if the string "vote" is in the tweet, skip it.
* implement a "delete all DM's" script (or ones that have been marked as read)


###stats:
I've been running the bot full time since 7/20/2016. So far I've won 1 contest.
