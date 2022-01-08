#Create Two Questions that you want to answer about the data:
#
#1. What was the Violent Murder crime rate in 2012 for the United States?
#		The answer was found to be 4.7
#
#2. What was the total amount of Violent Assault for New York in 2001?
#		The answer was found to be 98022



crimeFile = open("state_crime.csv", "r")
contents = crimeFile.read()
crimeFile.close()
headings = crimeFile.readline()
firstYear = crimeFile.readline()
infoList = []


#I opened the file, and read the first line in order to get the headings.
#The firstYear is just to read the second line to get the first line of data.
#I created an empty list of info list because I plan on looping through the
#rest of the information to find my answer in the question I asked. I will
#loop through the list once it has proper data.



for i in range(2750):
	line = crimeFile.readline()
	line = line.strip()
	line = line.replace('"', '')
	extraData = line.split(',')
	infoList.append(extraData)
#I looped through the remaining lines and "sanitized" the data for easy use.
#I put all the data into the empty list I created in the beginning.



crimeFile.close()
#I simply closed the file because I was done reading the file.
#I have extracted all the necessary data needed.



firstYear = firstYear.strip()
firstYear = firstYear.replace('"', '')
firstData = firstYear.split(',')
#This was to practice "sanitizing" data in the first line of data.



headings = headings.strip()
headings = headings.replace('"', '')
headingData = headings.split(',')
#I "sanitized" the header data that I will future need/use



for i in range(len(firstData)):
	if headingData[i] == 'State':
		state = firstData[i]
	if headingData[i] == 'Year':
		year = firstData[i]
	if headingData[i] == 'Data.Totals.Violent.Robbery':
		violentRobberyAmount = firstData[i]
#This was to practice accessing the data in the first line of
#data that I received.



for i in range(len(infoList)):
	for j in range(len(headingData)):
		if infoList[i][j] == 'United States' and infoList[i][j+1] == '2012':
			year = '2012'
			area = 'United States'
			index = i


#I wanted to access the information for the United States in the year of 2012.
#I looped through the data, and set the year to 2012 which is what we want.
#I then got the index value of the list and looped through it again later.



for k in range(len(infoList[index])):
	if headingData[k] == 'Data.Rates.Violent.Murder':
		murderCrimes = infoList[index][k]
#Here I looped through the list again, with the proper index and
#extracted the value that I needed. I needed the data rate for murder
#crimes in the United States in 2012 to answer my questions.

print('Question 1: What was the Violent Murder crime rate in 2012 for the United States?')
print('The data rates for violent murder crime in',\
 area, year, 'is', murderCrimes)
print()

for i in range(len(infoList)):
	for j in range(len(headingData)):
		if infoList[i][j] == 'New York' and infoList[i][j+1] == '2001':
			year = '2001'
			area = 'New York'
			index = i
#This loop I did the same thing as before.
#This time, however, I extracted the index where the year was
#New York and the year was 2001.



for k in range(len(infoList[index])):
	if headingData[k] == 'Data.Totals.Violent.All':
		assaultCrimes = infoList[index][k]
#This loops through the index with the data associated with New York and 2001.
#I extracted the total amount of assault crimes value for my answer.

print('Question 2: What was the total amount of Violent Assault for New York in 2001?')
print('The total amount of violent assault crimes in',\
 area, year, 'is', assaultCrimes)