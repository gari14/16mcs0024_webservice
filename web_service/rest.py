import pymongo
from pymongo import MongoClient
import json

import twitter
from pprintpp import pprint


'''
OAUTH
'''

CONSUMER_KEY      = "BgmgtBNn09WKIeXzOQM0xOg8e" # fill your oauth
CONSUMER_SECRET   = "mYex9vfLZmFyuwEMgJf4XaVb9rMIj4dDqC1W5M5wcX59XQZu6M" # fill your oauth
OAUTH_TOKEN       = "853536519738597376-X8v0W9bgWmMvDedrwbOMdOQnvhFaPBJ" # fill your oauth
OATH_TOKEN_SECRET = "woSLRxB0qPra1qPkMSuQiwn7Oy8zztpK75uJ7DvaZAViB" # fill your oauth

auth = twitter.oauth.OAuth(OAUTH_TOKEN,OATH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


'''
connect mongodb database
'''

client = MongoClient()

db = client.tweet_db

tweet_collection = db.tweet_collection
tweet_collection.create_index([("id", pymongo.ASCENDING)],unique = True)

'''
define query in REST API
'''
 
count = 500

geocode = "27.0696028,76.385523,500km"

 
q = " "
 
 
'''
fetch data
'''
  
search_results = twitter_api.search.tweets(q=q, count=count,geocode=geocode)
     
statuses = search_results["statuses"]
      
          
for statuse in statuses:
   try:
       tweet_collection.insert_many(statuse)
   except:
       pass
    
print (len(statuses))

'''
query collected data in MongoDB
'''
 
tweet_cursor = tweet_collection.find()
  
print (tweet_cursor.count())
  
user_cursor = tweet_collection.distinct("user.id")

print (len(user_cursor))
 
 
  
for document in tweet_cursor:
    try:
        print ('----')
#        pprint (document)
 
  
        print ('name:', document["user"]["name"])
        print ('text:', document["text"])
    except:
        print ("***error in encoding")
        pass
         
