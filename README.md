To aid in directory structure all datasets and their results have been split into folders, in a demo situation all files would most likely be kept in the main working directory where all .py files are located.

04_dataset_results_1 // 04_dataset_results_2 // 04_dataset_results_3 all contain the following:

## = filename in each directory (e.g. 'final' for '04_dataset_results_1')

##_age_ritp 		: Shows age compared to revealing info amounts.
##_agep 		: Shows age distribution percentage.
##_conf_int_screenshot 	: Shows confidence interval outputs.
##_female_ritp 		: Shows female likelihood of sharing revealing information.
##_gendp 		: Shows gender distribution percentage.
##_male_ritp 		: Shows male likelihood of sharing revealing information.
##_ritp 		: Shows overall likelihood of sharing information.


--------------------------------------------------------------------------------------------------------------------------

Usage Guide

--------------------------------------------------------------------------------------------------------------------------

Step 1
Ensure python 3.6 is installed and added to system path environment

Step 2
Ensure libraries are installed for all stages:
- run '#INSTALL_DEPENDENCIES#.bat'

Step 3
Open command prompt within the same directory as the python files

Step 4
Run 'python 1_tweetcollection.py' and follow instructions within program

Step 5
Run 'python 2_preprocess.py' and follow instructions within program, using output file from step 4 for input.

Step 6
Run 'python 3_genderage.py' and follow instructions within program, using output file from step 5 for input.

Step 7
Run 'python 4_cat-and-vis.py' and follow instructions within program, using output file from step 6 for input.

Step 8
View output from step 7:
- graphs saved as '.png' files.
- confidence intervals within the output of cmd in Step 7.

--------------------------------------------------------------------------------------------------------------------------
