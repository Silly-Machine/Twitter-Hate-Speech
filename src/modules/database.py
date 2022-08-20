from pymongo import MongoClient


class MongoDb:
    def __init__(self, hostname=None):
        self.base = MongoClient(hostname).twitterdb

    def write(self, tweet):
        try:
            self.base.tweets_raw.insert_one(tweet)
            return "data sucefully saved"

        except Exception:
            return "data unsucefully saved"
