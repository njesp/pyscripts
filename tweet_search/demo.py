"""
Get tweets
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

CONSUMER_KEY = 'SZ4ytote6u8Fx17prg2YrjRrs'
CONSUMER_SECRET = '80uvWs9k6EdwJlQSYlg6UuLfFYMc4pTmxjZfiEyzVuk9AxNxgv'
ACCESS_TOKEN = '18970184-PVLVstRfeOrh78t4Sy4amLdR3B8aAzySLDo4eghq5'
ACCESS_TOKEN_SECRET = 'Bpo0jylIUgEDRECMoFIpuQgJevvFKsBHp22NARMlXhLOR'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class StdOutListener(StreamListener):
    """
    Docstring
    """
    def on_data(self, raw_data):
        """
        Docstring
        """
        print(raw_data)
        return True

    def on_error(self, status_code):
        """
        Docstring
        """
        print(status_code)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, l)

    stream.filter(track=['#python', '#postgresql', '#postgres'])
