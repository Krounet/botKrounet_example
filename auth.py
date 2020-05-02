import tweepy
import re

def auth() :
	"""
	Twitter API Authentification
	"""
	auth_file=open("bot_id.txt")
	list_auth=auth_file.readlines()
	auth_file.close()
	list_auth_consumer=[key for key in list_auth if re.search('consumer',key)]
	list_auth_token=[key for key in list_auth if re.search('token',key)]
	
	
	
	#App consumer twitter keys
	consumer_key= [re.split('[ \n]',line)[1] for line in list_auth_consumer if re.search('key',line)][0]	
	consumer_secret= [re.split('[ \n]',line)[1] for line in list_auth_consumer if re.search('secret',line)][0]	
	
	#App access token twitter 
	access_token=[re.split('[ \n]',line)[1] for line in list_auth_token if re.search('secret',line)==None][0]	
	access_token_secret=[re.split('[ \n]',line)[1] for line in list_auth_token if re.search('secret',line)][0]	
	
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api = tweepy.API(auth)
	return api,auth


