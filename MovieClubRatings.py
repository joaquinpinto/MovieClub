#MovieClubRatings.py

#Import packages
import csv
import math

#Import Excel Sheet info into Dict
MovPrefDict = {}
MovList = []
with open('MovieRatings.csv', newline='') as f:
    reader = list(csv.reader(f))
    PersList = reader[0][1:]
    for i in PersList:
        MovPrefDict[i] = {}
    for row in reader[1:]:
        MovList.append(row[0])
        for j in range(1,len(row)):
            MovPrefDict[PersList[j-1]][row[0]] = int(row[j])


#Function to create Similarity Dict
SimDict = {}
ple = PersList[::]
totgroupdist = 0
for i in PersList:
	if len(ple) == 1:
		break
	if i not in SimDict.keys():
		SimDict[i] = {}
	ple.remove(i)
	for j in ple:
		if j not in SimDict.keys():
			SimDict[j] = {}
		counter = 0
		for mov in MovPrefDict[i]:
			counter += abs(MovPrefDict[i][mov] - MovPrefDict[j][mov])
		SimDict[i][j] = counter
		SimDict[j][i] = counter
		totgroupdist += counter


#Necessary Numbers
ml = len(MovList)
pl = len(PersList)
avggroupdist = totgroupdist/sum(range(1,pl+1))

# Create list of closest raters
used = []
closest = []
for pers in list(SimDict.keys()):
    used.append(pers)
    for comp in list(SimDict[pers].keys()):
        if not comp in used:
            closest.append((pers + " and " + comp, SimDict[pers][comp]))   

# Sort list of closest raters
closest.sort(key=lambda x: x[1])

# Print closest raters in order
print("\n Closest Raters \n")
for i in range(len(closest)):
	print(str(i+1) + ":", closest[i][0], "with an average distance of", round(closest[i][1]/ml, 2), "per movie")


#Distance from group
groupdistlist = []
for pers in list(SimDict.keys()):
	groupdist = 0
	for comp in list(SimDict[pers].keys()):
		groupdist += SimDict[pers][comp]
	groupdistlist.append((pers, groupdist))

# Sort list of closest raters
groupdistlist.sort(key=lambda x: x[1])


# Print avg distance from group in order
print("\n Average Group Distance \n")
for i in range(len(groupdistlist)):
	print(str(i+1) + ":", groupdistlist[i][0], "with an average distance of", round(groupdistlist[i][1]/((pl-1)*ml), 2), "from the group")