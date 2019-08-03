import re
import time
import pandas as pd
import numpy as np
from scipy.stats import sem, t #scipy for conf interval
from scipy import mean
from matplotlib import *
import matplotlib.pyplot as plt #matplotlib for pie charts
from ggplot import * #ggplot for bar charts

ay=0
a = []
epd_count = 0 #email count
accounts_c = 0 #account count
coordsf = 0 #coordinates count
pnumbers_pd = 0 #phone numbers in profile description count
pnumbers_t = 0 #phone numbers in tweet text
pnumberstot = 0 #total phone numbers count
total = 0 #total count of risky info found
male_c = 0 #males found count
female_c = 0 #females found count
ue = 0 #under 18 count (ignored)
etotn = 0 #18-29 count
tttofn = 0 #30-49 count
fttosf = 0 #50-64 count
sfo = 0 #over 65 count
numberst = 0

#genders
m_email_pd_ids = []
f_email_pd_ids = []
m_accounts_ids = []
f_accounts_ids = []
m_coords_ids = []
f_coords_ids = []
m_pnumbers_pd_ids = []
f_pnumbers_pd_ids = []
m_pnumbers_t_ids = []
f_pnumbers_t_ids = []


#ages
ag_email_pd_ids = []
nag_email_pd_ids = []
ag_accounts_ids = []
nag_accounts_ids = []
ag_coords_ids = []
nag_coords_ids = []
ag_pnumbers_pd_ids = []
nag_pnumbers_pd_ids = []
ag_pnumbers_t_ids = []
nag_pnumbers_t_ids = []

#age and gender
ma_email_pd_ids = []
fa_email_pd_ids = []
ma_accounts_ids = []
fa_accounts_ids = []
ma_coords_ids = []
fa_coords_ids = []
ma_pnumbers_pd_ids = []
fa_pnumbers_pd_ids = []
ma_pnumbers_t_ids = []
fa_pnumbers_t_ids = []

email_pd_ids = []
accounts_ids = []
coords_ids = []
pnumbers_pd_ids = []
pnumbers_t_ids = []



output_all = []
datetime = []
id = []
uname = []
sname = []
p_desc = []
loc = []
coords = []
orig = []
age = []
gender = []
codeid = []

phone_number = re.compile('(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?')
email = re.compile("""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
integer = re.compile("^[-+]?[0-9]+$")

print("")
print("James Frazer  -  1602294")
print("This code will finish categorisation and complete data visualisation")
print("")	

def main_menu():
	global ay
	global a
	global epd_count
	global accounts_c
	global coordsf
	global pnumbers_pd
	global pnumbers_t
	global pnumberstot
	global total
	global male_c
	global female_c
	global ue
	global etotn
	global tttofn
	global fttosf
	global sfo
	global numberst
	
	
	print("================================================")
	print("	Categorisation and Visualisation")
	print("================================================")
	print(" ")
	print("	1: Categorisation and Visualisation")
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
		
		def check_email(code_id):
			if re.search(email, p_desc[i]) is not None:
				email_pd_ids.append(code_id)
				if("Female" in gender[i]):
					f_email_pd_ids.append(code_id)
				if("Female" in gender[i] and "Yes" in age[i]):
					fa_email_pd_ids.append(code_id)
				elif("Male" in gender[i]):
					m_email_pd_ids.append(code_id)
				if("Male" in gender[i] and "Yes" in age[i]):
					ma_email_pd_ids.append(code_id)
				if("Yes" in age[i]):
					ag_email_pd_ids.append(code_id)
				else:
					nag_email_pd_ids.append(code_id)
				

		
		def check_accounts(code_id):
			if (('insta') in p_desc[i]):
				accounts_ids.append(code_id)
				if("Female" in gender[i]):
					f_accounts_ids.append(code_id)
				if("Female" in gender[i] and "Yes" in age[i]):
					fa_accounts_ids.append(code_id)
		
				elif("Male" in gender[i]):
					m_accounts_ids.append(code_id)
				if("Male" in gender[i] and "Yes" in age[i]):
					ma_accounts_ids.append(code_id)
		
				if("Yes" in age[i]):
					ag_accounts_ids.append(code_id)
				else:
					nag_accounts_ids.append(code_id)
			
			elif(('snapchat') in p_desc[i]):
				accounts_ids.append(code_id)
				if("Female" in gender[i]):
					f_accounts_ids.append(code_id)
				if("Female" in gender[i] and "Yes" in age[i]):
					fa_accounts_ids.append(code_id)
		
				elif("Male" in gender[i]):
					m_accounts_ids.append(code_id)
				if("Male" in gender[i] and "Yes" in age[i]):
					ma_accounts_ids.append(code_id)
		
				if("Yes" in age[i]):
					ag_accounts_ids.append(code_id)
				else:
					nag_accounts_ids.append(code_id)


		def check_coords(code_id):
			if('N/A' in coords[i]):
				ay = 0
			else:
				coords_ids.append(code_id)
				if("Female" in gender[i]):
					f_coords_ids.append(code_id)	
				if("Female" in gender[i] and "Yes" in age[i]):
					fa_coords_ids.append(code_id)
			
				elif("Male" in gender[i]):
					m_coords_ids.append(code_id)
				if("Male" in gender[i] and "Yes" in age[i]):
					ma_coords_ids.append(code_id)
			
				if("Yes" in age[i]):
					ag_coords_ids.append(code_id)
				else:
					nag_coords_ids.append(code_id)
		
		def check_phone(code_id):
			if re.search(phone_number, p_desc[i]) is not None:
				pnumbers_pd_ids.append(code_id)
				if("Female" in gender[i]):
					f_pnumbers_pd_ids.append(code_id)
				if("Female" in gender[i] and "Yes" in age[i]):
					fa_pnumbers_pd_ids.append(code_id)
				elif("Male" in gender[i]):
					m_pnumbers_pd_ids.append(code_id)
				if("Male" in gender[i] and "Yes" in age[i]):
					ma_pnumbers_pd_ids.append(code_id)
		
				if("Yes" in age[i]):
					ag_pnumbers_pd_ids.append(code_id)
				else:
					nag_pnumbers_pd_ids.append(code_id)
			elif re.search(phone_number, output_all[i]) is not None:
				pnumbers_t_ids.append(code_id)
				if("Female" in gender[i]):
					f_pnumbers_t_ids.append(code_id)
				if("Female" in gender[i] and "Yes" in age[i]):
					fa_pnumbers_t_ids.append(code_id)
				elif("Male" in gender[i]):
					m_pnumbers_t_ids.append(code_id)
				if("Male" in gender[i] and "Yes" in age[i]):
					ma_pnumbers_t_ids.append(code_id)
		
				if("Yes" in age[i]):
					ag_pnumbers_t_ids.append(code_id)
				else:
					nag_pnumbers_t_ids.append(code_id)

		for line in open(tweets_filename+'.txt', encoding="utf8").readlines():
			if "Coded ID:" in line:
				codeid.append(line.replace('Coded ID:', ''))	
			elif "Date/Time:" in line:
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
			elif "Pre-processed" in line:
				output_all.append(line.replace('Pre-processed Tweet Text:', ''))
			elif "Tweet Text:" in line:
				orig.append(line)
			elif "Age Given:" in line:
				age.append(line)
			elif "Gender:" in line:
				gender.append(line)


		
		for i in range(0, len(output_all)):
			check_email(codeid[i])
			check_accounts(codeid[i])
			check_coords(codeid[i])
			check_phone(codeid[i])



			
		epd_count = len(email_pd_ids)
		accounts_c = len(accounts_ids)
		coordsf = len(coords_ids)
		pnumbers_pd = len(pnumbers_pd_ids)
		pnumbers_t = len(pnumbers_t_ids)
		pnumberstot = pnumbers_pd + pnumbers_t

		total = epd_count + accounts_c + coordsf + pnumberstot
		m_total = len(m_email_pd_ids) + len(m_accounts_ids) + len(m_coords_ids) + len(m_pnumbers_pd_ids) + len(m_pnumbers_t_ids)
		f_total = len(f_email_pd_ids) + len(f_accounts_ids) + len(f_coords_ids) + len(f_pnumbers_pd_ids) + len(f_pnumbers_t_ids)
		ma_total = len(ma_email_pd_ids) + len(ma_accounts_ids) + len(ma_coords_ids) + len(ma_pnumbers_pd_ids) + len(ma_pnumbers_t_ids)
		fa_total = len(fa_email_pd_ids) + len(fa_accounts_ids) + len(fa_coords_ids) + len(fa_pnumbers_pd_ids) + len(fa_pnumbers_t_ids)
		
		for i in range(0,len(output_all)):
			if("Female" in gender[i]):
				female_c = female_c + 1
			else:#("male" in gender[i]):
				male_c = male_c + 1

		
		for i in range(0,len(output_all)):
			if("Yes" in age[i]):
		
				if re.findall('\d+', p_desc[i]) is not None:
					numbers=re.findall('\d+', p_desc[i])
					for ay in numbers:
						numberst = int(numbers[0])
			
					if(numberst < 18):
						ue = ue + 1 #under 18
					elif(numberst > 17 and numberst < 30):
						etotn = etotn + 1 #18-29
					elif(numberst > 29 and numberst < 50):
						tttofn = tttofn + 1 #30-49
					elif(numberst > 49 and numberst < 65):
						fttosf = fttosf + 1 #50-64
					elif(numberst > 64):
						sfo = sfo + 1 #65 and over
	
		atotal = etotn + tttofn + fttosf + sfo
			
		alabels = '18-29', '30-49', '50-64', '65+' #names
		asizes = [etotn/atotal*100, tttofn/atotal*100, fttosf/atotal*100, sfo/atotal*100] #numbers
		acolors = ['gold','yellowgreen','lightcoral','orchid']
		aexplode = (0.1, 0.1, 0.1, 0.1)
		
		plt.pie(asizes, explode=aexplode, labels=alabels, colors=acolors, autopct='%1.1f%%', shadow=True, startangle=140)
		plt.axis('equal')
		plt.savefig(str(tweets_filename)+"_agep.png")
		plt.close()
		
		glabels = 'Male', 'Female'
		gsizes = [(male_c/(male_c+female_c))*100,(female_c/(male_c+female_c))*100]
		gcolors = ['blue','pink']
		gexplode = (0.1,0.1)
		
		plt.pie(gsizes, explode=gexplode, labels=glabels, colors=gcolors, autopct='%1.1f%%', shadow=True, startangle=140)
		plt.axis('equal')
		plt.savefig(str(tweets_filename)+"_gendp.png")
		plt.close()
			
			
			
			
		#data frames
		ritp_df = pd.DataFrame({"Type":["Emails(PD)","Accounts(PD)","Coords", "PNumbers"], "%":[(epd_count/total)*100,(accounts_c/total)*100,(coordsf/total)*100,(pnumberstot/total)*100]})
		#gendp_df = pd.DataFrame({"Gender":["Male", "Female"], "%":[(male_c/100000)*100, (female_c/100000)*100]})
		male_ritp_df = pd.DataFrame({"Type":["Emails(PD)","Accounts(PD)","Coords", "PNumbers"], "Amount":[len(m_email_pd_ids)/m_total*100,len(m_accounts_ids)/m_total*100,len(m_coords_ids)/m_total*100,(len(m_pnumbers_pd_ids)+len(m_pnumbers_t_ids))/m_total*100]})
		female_ritp_df = pd.DataFrame({"Type":["Emails(PD)","Accounts(PD)","Coords", "PNumbers"], "Amount":[len(f_email_pd_ids)/f_total*100,len(f_accounts_ids)/f_total*100,len(f_coords_ids)/f_total*100,(len(f_pnumbers_pd_ids)+len(f_pnumbers_t_ids))/f_total*100]})
		#agep_df = pd.DataFrame({"Age Group":["18-29", "30-49", "50-64", "65+"], "%":[etotn/atotal*100, tttofn/atotal*100, fttosf/atotal*100, sfo/atotal*100]})
		age_ritp_df = pd.DataFrame({"Type":["Emails(PD)","Accounts(PD)","Coords", "PNumbers"], "Amount":[len(ag_email_pd_ids), len(ag_accounts_ids), len(ag_coords_ids), (len(ag_pnumbers_pd_ids)+len(ag_pnumbers_t_ids))]})
		#age_genderp_df = pd.DataFrame({"Gender":["Male", "Female"], "%":[(ma_total/male_c), (fa_total/female_c)]})
		#age_gender_ritp_df = pd.DataFrame()


		#ggplots
		ritp = ggplot(aes(x="Type", y="%", weight="%"), data=ritp_df) + geom_bar(fill='green') +ggtitle("Revealing Information")+ ylim(0,100)
		#gendp = ggplot(aes(x="Gender", y="%", weight="%"), data=gendp_df) + geom_bar(fill='green') + ggtitle("% of Male and Female Twitter Users") + ylim(0,100)
		male_ritp = ggplot(aes(x="Type", y="Amount", weight="Amount"), data=male_ritp_df) + geom_bar(fill='blue') + ggtitle("Males Revealing Information") + ylim(0,100)
		female_ritp = ggplot(aes(x="Type", y="Amount", weight="Amount"), data=female_ritp_df) + geom_bar(fill='pink') + ggtitle("Females Revealing Information") + ylim(0,100)
		#agep = ggplot(aes(x="Age Group", y="%", weight="%"), data=agep_df) + geom_bar(fill='green') + ggtitle("Age Group % of Twitter Users*") + ylim(0, 100)
		age_ritp = ggplot(aes(x="Type", y="Amount", weight="Amount"), data=age_ritp_df) + geom_bar(fill='green') + ggtitle("Ages Revealing Information")

		#file names
		ritp_file_name = (str(tweets_filename)+"_ritp.png")
		#gendp_file_name = (str(tweets_filename)+"_gendp.png")
		male_ritp_file_name = (str(tweets_filename)+"_male_ritp.png")
		female_ritp_file_name = (str(tweets_filename)+"_female_ritp.png")
		#agep_file_name = (str(tweets_filename)+"_agep.png")
		age_ritp_file_name = (str(tweets_filename)+"_age_ritp.png")

		#save file
		ritp.save(ritp_file_name)
		#gendp.save(gendp_file_name)
		male_ritp.save(male_ritp_file_name)
		female_ritp.save(female_ritp_file_name)
		#agep.save(agep_file_name)
		age_ritp.save(age_ritp_file_name)
		
		### CODE BELOW DOES CONFIDENCE INTERVAL ###
		g = [male_c, female_c]
		a = [etotn, tttofn, fttosf, sfo]
		mri = [len(m_email_pd_ids), len(m_accounts_ids), len(m_coords_ids), len(m_pnumbers_pd_ids)+len(m_pnumbers_t_ids)]
		fri = [len(f_email_pd_ids), len(f_accounts_ids), len(f_coords_ids), len(f_pnumbers_pd_ids)+len(f_pnumbers_t_ids)]
		confidence = 0.95
		
		glen=len(g)
		alen=len(a)
		mrilen=len(mri)
		frilen=len(fri)
		
		gmean=mean(g)
		amean=mean(a)
		mrimean=mean(mri)
		frimean=mean(fri)
		
		gstd_err=sem(g)
		astd_err=sem(a)
		mristd_err=sem(mri)
		fristd_err=sem(fri)
		
		hg = gstd_err * t.ppf((1 + confidence) / 2, glen - 1)
		ha = astd_err * t.ppf((1 + confidence) / 2, alen - 1)
		hmri = mristd_err * t.ppf((1 + confidence) / 2, mrilen - 1)
		hfri = fristd_err * t.ppf((1 + confidence) / 2, frilen - 1)
		
		gstart = gmean - hg
		gend = gmean + hg
		astart = amean - ha
		aend = amean + ha
		mristart = mrimean - hmri
		mriend = mrimean + hmri
		fristart = frimean - hfri
		friend = frimean + hfri
		
		print("Gender")
		print(gstart)
		print(gend)
		print("---------------")
		print("Age")
		print(astart)
		print(aend)
		print("---------------")
		print("Males Revealing Info")
		print(mristart)
		print(mriend)
		print("---------------")
		print("Females Revealing Info")
		print(fristart)
		print(friend)
		

		###Need CI for - Gender, Age, RITP, G/RITP? & A/RITP?###
		
	elif(x == "2"):
		exit()
		
	else:
		print("Invalid Input")
		time.sleep(2)
		main_menu()	
		
main_menu()