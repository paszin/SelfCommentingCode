import random
import hackercomments

opinions = ["This is amazing", "Awesome", "Ugly Code", "Fancy Hack"]
def getRandomOpinion():
	return random.choice(opinions)

adjectives = ["famous", "popular", "advanced", "radical", "under-appreciated"]
def getRandomAdjective():
	return random.choice(adjectives)

varMeanings = ["stores the state of the process", "is used for seed data", "contains all filtered objects", "is a semaphores tor thread locking"]
def getRandomMeaning():
	return random.choice(varMeanings)

def getRandomHackerComment():
	return random.choice(hackercomments.data)


