import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import time
from html.parser import HTMLParser


consumer_key = ''
consumer_secret = ''
access_token =  ''
access_secret = ''


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

print("")
print("James Frazer  -  1602294")
print("This code will collect tweets from twitter using Streaming API.")
print("")

def main_menu():
	print("===============================")
	print("	Data Collection")
	print("===============================")
	print(" ")
	print("	1: Run Data Collection")
	print("	2: Exit")
	print(" ")
	print("Please enter your choice:")
	x = input()
	if(x == "1"):
		
		print(" ")
		print("Please enter the desired output file name (will be given .txt extension)")
		print("Please ensure the filename contains valid characters:")
		user_filename = input()
		print(" ")
		print("To stop code running please close this window.")
		time.sleep(2)
		class MyListener(StreamListener):

			def on_data(self, data):
		
				try:
					with open(user_filename+'.txt', 'a', encoding="utf-8") as f: #'tweets_unp-coord-25-ds3.txt'
						count = 1
						all_data = json.loads(HTMLParser().unescape(data))
				
						dtime = all_data.get('created_at','')
						id = all_data.get('id_str','')
						user = all_data.get('user','')
						username = user.get('name','')
						sname = user.get('screen_name','')
						bio = user.get('description','')
						location = "N/A"
						coordinates = "N/A"
				
				
						if user.get('location',None) is not None:
							location = user.get('location','')
				
						if all_data.get('coordinates', None) is not None:
							latitude, longitude = all_data['coordinates']['coordinates']
							coordinates = str(latitude) +","+ str(longitude)
							##wrong order used here - FUTURE WORK

			
				
						tweet = all_data.get('text','')
						relevant_data = "Date/Time:" + dtime + "\nID: " + id + "\nUser Name: " + username + "\nScreen Name: " + sname + "\nDescription: " + bio + "\nLocation: " + location + "\nCoordinates: " + coordinates + "\nTweet Text: " + tweet + "\n"
				
				
				
						f.write("\n")
						f.write(relevant_data)
						f.write("\n")
						return True
				except BaseException as e:
					return True#print("Error on_data: %s" % str(e))
				#return True
 
			def on_error(self, status):
				print(status)
				return True
				if status==420:
					return False
 
		twitter_stream = Stream(auth, MyListener())
		twitter_stream.filter(languages=["en"], track=['the', 'i', 'to', 'a', 'and', 'is', 'in', 'it', 'you', 'of', 'for', 'on', 'my', 'that', 'at' , 'with', 'me', 'do', 'have', 'just', 'this', 'be', 'so', 'are', 'not'])#, 'was', 'but', 'out', 'up', 'what', 'now', 'new', 'from', 'your', 'like', 'good', 'no', 'get', 'all', 'about', 'we', 'if', 'time', 'as', 'day', 'will', 'one', 'twitter', 'how', 'can', 'some', 'an', 'am', 'by', 'going', 'they', 'go', 'or', 'has', 'rt', 'know', 'today', 'there', 'love', 'more', 'work', 'too', 'got', 'he', 'back', 'think', 'did', 'lol', 'when', 'see', 'really', 'had', 'great', 'off', 'would', 'need', 'here', 'thanks', 'been', 'still', 'people', 'blog', 'who', 'night', 'want', 'why', 'home', 'should', 'well', 'oh', 'much', 'u', 'then']) # uses 100 of most common twitter phrases (some were swapped for ones further down in list but number is 100)
		
	elif(x == "2"):
		exit()
	else:
		print("Invalid Input")
		time.sleep(2)
		main_menu()

		
main_menu()

