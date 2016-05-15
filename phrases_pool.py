import random

opinions = ["This is amazing", "Awesome", "Ugly Code", "Fancy Hack"]
def getRandomOpinion():
	return random.choice(opinions)

adjectives = ["famous", "popular", "advanced"]
def getRandomAdjective():
	return random.choice(adjectives)

varMeanings = ["stores the state of the process", "is used for seed data", "contains all filtered objects"]
def getRandomMeaning():
	return random.choice(varMeanings)