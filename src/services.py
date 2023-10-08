from typing import Any, Dict, List
import tweepy
from src.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from src.constants import BRAZIL_WOE_ID
from src.connection import trends_collection

def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]: 
    breakpoint()
    trends = api.get_place_trends(woe_id)
        
    return trends[0]["trends"]
    
    
def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)
    

def save_trends() -> None:
    
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    
    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)