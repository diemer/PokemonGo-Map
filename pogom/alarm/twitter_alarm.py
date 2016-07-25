import logging

from alarm import Alarm, gmaps_link, pkmn_time_text
import tweepy


log = logging.getLogger(__name__)

class Twitter_Alarm(Alarm):
	
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.client = tweepy.API(auth)

        log.info("Tweepy intialized.")

    def send_tweet(self, message):
        self.client.update_status(message)


    def pokemon_alert(self, pokemon):
        google_maps_link = gmaps_link(pokemon["lat"], pokemon["lng"])
        time_text =  pkmn_time_text(pokemon['disappear_time'])
        notification_text = "A wild " + pokemon['name'].title() + " has appeared!"
        self.send_tweet(notification_text + " " + time_text + " " + google_maps_link)
