from st2common.runners.base_action import Action
from TwitterSearch import *
from st2client.client import Client
from st2client.models import KeyValuePair
client = Client(base_url='http://localhost')

class BaseAction(Action):
    def match_tweet(self,expected_string):
        tuo = TwitterUserOrder(self.config['twitter_user_id']) # create a TwitterUserOrder
        
        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(
            consumer_key = self.config['consumer_key'],
            consumer_secret = self.config['consumer_secret'],
            access_token = self.config['access_token'],
            access_token_secret = self.config['access_token_secret']
        )
        tweet_id = client.keys.get_by_name(name='tweet_id')
        tweet_id = tweet_id.value        
        # start asking Twitter about the timeline
        for tweet in ts.search_tweets_iterable(tuo):
            if tweet['id']>int(tweet_id):
                if tweet['text'] == expected_string:
                    client.keys.update(KeyValuePair(name='tweet_id', value = str(tweet['id'])))
                    return True,True,"String matched"
        return True,False,"String not matched"

