import nltk
import time
import re
from nltk.corpus import names
import random

um_count = 0
uf_count = 0
sm_count = 0
sf_count = 0
agecount = 0
tagecount = 0
output_all = []
datetime = []
id = []
uname = []
sname = []
p_desc = []
loc = []
coords = []
orig = []
genders = []
agefound = []

date = re.compile("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$")

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE) ###FUTURE WORK - do in pre-processing stage along with other techniques for all 3 used fields

print("")
print("James Frazer  -  1602294")
print("This code will add a coded ID to each user, as well as define age and gender where applicable.")
print("")						   
						   					   
def main_menu():
	global um_count
	global uf_count
	global sm_count
	global sf_count
	global agecount
	global tagecount

	print("=============================================")
	print("	Gender and Age Categorisation")
	print("=============================================")
	print(" ")
	print("	1: Run Gender and Age Categorisation")
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
	
	
	
		for line in open(tweets_filename+".txt", encoding="utf8").readlines():
			if "Date/Time:" in line:
				datetime.append(line)
			elif "ID:" in line:
				id.append(line)
			elif "User Name:" in line:
				line =emoji_pattern.sub('',line)
				uname.append(line.strip().replace('User Name: ', ''))
			elif "Screen Name:" in line:
				sname.append(line.strip().replace('Screen Name: ', ''))
			elif "Description:" in line:
				p_desc.append(line)
			elif "Location:" in line:
				loc.append(line)
			elif "Coordinates:" in line:
				coords.append(line)
			elif "Pre-processed" in line:
				output_all.append(line.replace('Pre-processed Tweet Text', ''))
			elif "Tweet Text:" in line:
				orig.append(line)
		
		def gender_features(word):
			return {'last_letter': word[-1],
			'last_two_letters': word[-2:]}

		labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
		random.shuffle(labeled_names)

		featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
		train_set, test_set = featuresets[int(len(featuresets)*4/5):], featuresets[:int(len(featuresets)*4/5)] #500
		classifier = nltk.NaiveBayesClassifier.train(train_set) ##average of 81% accuracy

		for i in range (0, len(output_all)):
			if(classifier.classify(gender_features(uname[i])) == 'male'):
				um_count = um_count + 1
				genders.append("Male")
			if(classifier.classify(gender_features(uname[i])) == 'female'):
				uf_count = uf_count + 1
				genders.append("Female")		
			
			if (re.search(date, p_desc[i]) is not None) or (("years old") in p_desc[i]):
				agecount = agecount + 1
				agefound.append("Yes")
			else:
				agefound.append("No")
	
		fh = open(output_filename+'.txt','w', encoding="utf-8")
		for i in range(0,len(output_all)):
			userdetails = "Coded ID: " + str(i+1) + "\n" + datetime[i] + id[i] + "User Name: " + uname[i]+"\n" + "Screen Name:" + sname[i] +"\n"+ p_desc[i] + loc[i] + coords[i] + orig[i] + "Pre-processed Tweet Text: "+ output_all[i] + "Gender: " + genders[i] + "\n" + "Age Given: " + agefound[i]
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