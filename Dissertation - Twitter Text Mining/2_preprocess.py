import re
import sys
import json
import string
import nltk
import time
nltk.download('punkt')		## Only needed if running for the first time on a new system
nltk.download('stopwords') ## Only needed if running for the first time on a new system
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

#preprocessing setup
tknzr= TweetTokenizer(strip_handles=True, reduce_len=False)
punctuation=list(string.punctuation)
swords=stopwords.words('english')
LOG_EVERY_N = 1000
tokens = []
tweets = []

#storage for all data
output_all = []
datetime = []
id = []
uname = []
sname = []
p_desc = []
loc = []
coords = []


print("")
print("James Frazer  -  1602294")
print("This code will pre-process tweets from file.")
print("")

def main_menu():
	print("====================================")
	print("	Data Pre-processing")
	print("====================================")
	print(" ")
	print("	1: Run Data Pre-processing")
	print("	2: Exit")
	print(" ")
	print("Please enter your choice:")
	x = input()
	if(x == "1"):
		print(" ")
		print("Please enter the input file name (.txt extension will be added)")
		print("Please ensure the filename contains valid characters and exists in directory:")
		tweets_filename = input()
		print(" ")
		time.sleep(1)
		print("Please enter the output file name (.txt extension will be added)")
		print("Please ensure the filename contains valid characters:")
		output_filename = input()
		print(" ")
		time.sleep(1)
		
		#store all
		for line in open(tweets_filename+".txt", encoding="utf8").readlines():
			if "Date/Time:" in line:
				datetime.append(line)
			elif "ID:" in line:
				id.append(line)
			elif "User Name:" in line:
				uname.append(line)
			elif "Screen Name:" in line:
				sname.append(line)
			elif "Description:" in line:
				p_desc.append(line)
			elif "Location:" in line:
				loc.append(line)
			elif "Coordinates:" in line:
				coords.append(line)
			elif "Tweet Text:" in line:
				output_all.append(line.replace('Tweet Text:', ''))
		
		print("This process takes a while depending on file size. The program will output the number preprocessed every 1000.")
		time.sleep(2)
		
		#apply preprocessing techniques to tweet text before saving
		for i in range(0, len(output_all)):
			tokens.append(tknzr.tokenize(output_all[i]))
			tokens[i] = [term for term in tokens[i] if term.lower() not in set (swords)]
			tweets = [[','.join(i)] for i in tokens]
			if (i % LOG_EVERY_N) == 0:
				print(i)	

		fh = open(output_filename+'.txt','w', encoding="utf-8")
		for i in range(0,len(output_all)):
			userdetails = datetime[i] + id[i] + uname[i] + sname[i] + p_desc[i] + loc[i] + coords[i] + "Tweet Text: "+ output_all[i] + "Pre-processed Tweet Text: "+','.join(map(str.lower,tweets[i]))
			fh.write(userdetails)
			fh.write("\n")
			fh.write("\n")
	
		fh.close()
		
	elif(x == "2"):
		exit()
	else:
		print("Invalid Input")
		time.sleep(2)
		main_menu()

		
main_menu()