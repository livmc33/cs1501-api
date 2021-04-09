
import tweepy


auth = tweepy.OAuthHandler("XNiGWt1nJoVnyJzrkq9iLGePO", "e6JPGSAEDBfCMid4NIuaIFv0RfIRW7FcaNM0MtvxXSxvfhR666")
auth.set_access_token("841391099184832513-11wSV8Ak91MHmE6c84eJcyvoxFY4UY9", "PBf32e0LLoeXjGopDfp80xp4YXuCQPEqPDfFr8mkIjQj0")

api = tweepy.api(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(f"{tweet.user.name} said {tweet.text}")
