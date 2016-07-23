"""
Created on 18 Jul 2016 at 21:17
@author ckan
"""
import os
import json
import re
from datetime import datetime
import pandas as pd # pandas for data analysis/manipulation
import matplotlib.pyplot as plt # matplotlib for data visualization


class TweetExtractor:
	"""
		Tweeter extractor
        Extract a value For each key within a tweet
	"""
	def extract(self, key, tweets):
		data = []
		for tweet in tweets:
			self.depth_search(lookup=key, tweet=tweet, data=data)
		return data

	def depth_search(self, lookup, tweet, data):
		if isinstance(tweet, dict):
			for key in tweet.keys():
				value = tweet[key]

				if value == None:
					data.append(None)
				else:
					if lookup == key:
						if isinstance(value, unicode) or isinstance(value, str):
							data.append(value)
							#break
						elif isinstance(value, dict): # k = dict
							print value
					else:
						self.depth_search(lookup, value, data)

					#else:	
						# k = list
						#print 'do nothing'

	def first_level_extraction(self, key, tweets):
		""" Extraction de niveau 1
			Retourne sous forme de liste les valeurs des cles de niveau 1
		"""
		data = []
		for tweet in tweets:
			self.__first_level_extraction(lookup=key, tweet=tweet, data=data)
		return data

	def __first_level_extraction(self, lookup, tweet, data):
		if isinstance(tweet, dict):
			for key in tweet.keys():
				if lookup == key and isinstance(key, unicode):
					data.append(tweet[key])
					break

	def second_level_extraction(self, first_level_key, key, tweets):
		""" Extraction de niveau 2
			Retourne sous forme de liste les valeurs des cles de niveau 2
		"""
		data = []
		for tweet in tweets:
			self.__second_level_extraction(lookup=key, first_level_key=first_level_key, tweet=tweet, data=data)
		return data

	def __second_level_extraction(self, first_level_key, lookup, tweet, data):
		if isinstance(tweet, dict):
			for key in tweet.keys():
				if first_level_key == key:
					value = tweet[key]
					if value == None:
						data.append(None)
					else:
						if isinstance(value, unicode):
							data.append(value)
						elif isinstance(value, dict):
							self.__second_level_extraction(lookup, None, value, data)

class DataViz:
    """
        Data Visualization
        Allow the data visualization
    """
    @staticmethod
    def visualize(df, x_label, y_label, plot_title, color):
        # create a figure object with a set of subplots, here one subplot        
        fig, ax = plt.subplots()
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_xlabel(x_label, fontsize=15)
        ax.set_ylabel(y_label, fontsize=15)
        ax.set_title(plot_title, fontsize=15, fontweight='bold')
        df.plot(ax=ax, kind='bar', color=color)
    
    @staticmethod
    def plot_grid(x_labels, y, title):
        x_pos = list(range(len(x_labels)))
        width = 0.8
        fig, ax = plt.subplots()
        plt.bar(left=x_pos, height=y, width=width, color='g')

        ax.set_ylabel('Numbers of tweets', fontsize=15)
        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.set_xticks([w + 0.4 * width for w in x_pos])
        ax.set_xticklabels(x_labels)
        plt.grid()
        
def word_in_text(word, text):
    found = False
    if re.search(word.lower(), text.lower()):
        found = True    
    return found

def extract_link(text):
    """
    Extract a link in a text
    """
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return None

""" Taille du fichier au moment de l'analyse: 103, 807 Ko """
#filename = os.path.join(os.getcwd(), 'data', 'twitter_data.json')
filename = os.path.join(os.getcwd(), 'data', 'twitter_data.json')
data = open(filename, 'r')

start = datetime.now()
tweets_data = [json.loads(tweet) for tweet in data]
print 'Tweets total : ', len(tweets_data)

# programming languages
prgs = {'java':'java', 'csharp':'c#', 'php':'php', 'python':'python', 'ruby': 'ruby', 'js' : 'javascript'}

tweetExtractor = TweetExtractor()

tweets_df = pd.DataFrame() # Empty tweets DataFrame

# fill the dataFrame with values
tweets_df['text'] = tweetExtractor.first_level_extraction(key=u'text', tweets=tweets_data)
tweets_df['lang'] = tweetExtractor.first_level_extraction(key=u'lang', tweets=tweets_data)
tweets_df['country'] = tweetExtractor.second_level_extraction(first_level_key='place', 
                        key=u'country', tweets=tweets_data)

tweets_by_lang = tweets_df['lang'].value_counts()
tweets_by_country = tweets_df['country'].value_counts()

DataViz.visualize(df=tweets_by_lang[:6], x_label='Languages', y_label='Numbers of tweets', 
                 plot_title='Top 5 Languages', color='red')
DataViz.visualize(df=tweets_by_country[:6], x_label='Countries', y_label='Numbers of tweets', 
                plot_title='Top 5 countries', color='blue')

"""
The goal of this text mining is to compare the popularity of the programming 
languages such as: Java, Javascript, ruby, c#, python
"""
# ######################################################
prg_langs = [prg for prg in prgs.values()]

for word in prg_langs:
    tweets_df[word] = tweets_df['text'].apply(lambda text : word_in_text(word, text))

tweets_by_prg_langs = [tweets_df[prg].value_counts()[True] for prg in prg_langs]

title = 'Ranking of '
for i in range(len(prg_langs)):
    title = title + prg_langs[i]
    if i == len(prg_langs) - 1:
        break
    title = title + ' vs '

DataViz.plot_grid(x_labels=prg_langs, y=tweets_by_prg_langs, title=title)


tweets_df['programming'] = tweets_df['text'].apply(lambda text : word_in_text('programming', text))
tweets_df['tutorial'] = tweets_df['text'].apply(lambda text : word_in_text('tutorial', text))
tweets_df['relevant'] = tweets_df['text'].apply(lambda text: word_in_text('programming', text) 
        or word_in_text('tutorial', text))


relevents_tweets_by_prg_langs = [tweets_df[tweets_df['relevant'] == True][prg].value_counts()[True] for prg in prg_langs]
DataViz.plot_grid(x_labels=prg_langs, y=relevents_tweets_by_prg_langs, title=title + ' (Relevant data)')

tweets_df['link'] = tweets_df['text'].apply(lambda text : extract_link(text))

relevants_tweets = tweets_df[tweets_df['relevant'] == True]
relevants_links = relevants_tweets[relevants_tweets['link'] != None]

df = relevants_links[relevants_links['relevant'] == True]
#print df.head()

for prg in prg_langs:
    print relevants_links[relevants_links[prg] == True][prg].value_counts()


end = datetime.now()

print 'elapsed time : ', str(end - start)