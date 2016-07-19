"""
Created on 17 Jul. 2016 at 22:18
@author ckan
"""

"""
We are going to use 'The Twitter streaming API' which is used 
to download twitter messages in real time
see: http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
For authentication/authorization see: http://docs.tweepy.org/en/v3.4.0/auth_tutorial.html#auth-tutorial
"""

from util import CredentialsReader
from util import ArgParser
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import os
import sys


datafile = os.path.join(os.getcwd(), 'data', 'twitter_data.json')

class OutputListener(StreamListener):
	def on_data(self, data):
		with open(datafile, 'a') as tf:
			tf.write(data)
		return True

	def on_status(self, status):
		#print 'Inside on_status'
		print status.text

	def on_error(self, status):
		#print 'Inside on_error'
		print status
		return False


def main():
	args = ArgParser.parse()
	#print 'credentials filename : ', args.credentials
	if args.credentials != None:

		print '********* Retreive credentials ****************'
		credentials = CredentialsReader.read(args.credentials)
		consumer_key = credentials['consumer_key']
		consumer_secret = credentials['consumer_secret']
		access_token = credentials['access_token']
		access_token_secret = credentials['access_token_secret']

		print '********* Twitter Authentication ***********'
		# Twitter authentification
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)

		ol = OutputListener() # instance of OutputListener
		stream = Stream(auth=auth, listener=ol)

		# Start a stream
		print '************** Start a stream *****************'
		if args.kw_file != None and len(args.args_list) == 0:
			keywords = []
			with open (os.path.join(os.getcwd(), args.kw_file), 'r') as f:
				keywords = f.readlines()
			keywords = [x.strip('\n') for x in keywords]
			#print 'kewords from file: ', keywords
			stream.filter(track=keywords)
		elif args.kw_file is None and len(args.args_list) > 0:
			#print'args list:',  args.args_list
			stream.filter(track=args.args_list)
		else:
			print 'Impossible d\'utiliser les deux options en meme temps'


if __name__ == '__main__':
	"""keywords = []
	with open (os.path.join(os.getcwd(), sys.argv[1]), 'r') as f:
		keywords = f.readlines()
	keywords = [x.strip('\n') for x in keywords]"""
	#print keywords
	#print '*** calling main() method ****'
	main()

