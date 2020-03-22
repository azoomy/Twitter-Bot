import tweepy
import logging
import os
import TB_credentials

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv(TB_credentials.CONSUMER_KEY)
    consumer_secret = os.getenv(TB_credentials.CONSUMER_SECRET)
    access_token = os.getenv(TB_credentials.ACCESS_TOKEN)
    access_token_secret = os.getenv(TB_credentials.ACCESS_TOKEN_SECRET)
    auth = tweepy.OAuthHandler(TB_credentials.CONSUMER_KEY, TB_credentials.CONSUMER_SECRET)
    auth.set_access_token(TB_credentials.ACCESS_TOKEN, TB_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api