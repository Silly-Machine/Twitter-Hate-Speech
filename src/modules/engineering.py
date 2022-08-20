import json


def TweetJson(tweet, query=None):
    json_dump = json.dumps(tweet._json)
    json_tweet = json.loads(json_dump)
    json_tweet["query"] = query

    return json_tweet
