# Rank and weighted random order

"""
Plan is to assign a certain number of lottery balls to each movie depending on their position

Each movie begins with 1 lottery ball

We will then add a ball for each movie's rank

1: +1
1-5: +1
1-10: +1
1-20: +1
1-30: +1
1-40: +1
1-50: +1
1-100: +1

If there’s a tie, the movie is counted in the better group.
"""

# Import to read csv
import csv
import random

# Put movies into dictionary with value of [adjAvg, 1]
MovDict = {}
with open('AdjustedMovieAverage.csv', newline='') as f:
	reader = list(csv.reader(f))
	for i in range(1,len(reader)):
		MovDict[reader[i][1]] = [float(reader[i][2]), 1]

# Create new dictionary for only movies we will watch
# We will only watch movies with a greater than 5 rating
MovDictRanker = {}
for i in MovDict.keys():
	if MovDict[i][0] >= 5:
		MovDictRanker[i] = MovDict[i]

# Find where lottery adder ends
rankend = len(MovDictRanker)
rankgroup = [1, 5, 10, 20, 30, 40, 50, 100, 150, 200, 250]
stopper = 0
for i in range(len(rankgroup)):
	if rankend > rankgroup[i]:
		stopper += 1
	else:
		break


# Rank values then assign points to each movie depending on value
rv = list(MovDictRanker.values())
Ranker_values = []
for i in rv:
	Ranker_values.append(i[0])

# Sort values by descending order
Ranker_values.sort(reverse=True)

# Go through MovDictRanker, add 1 to the second part of the list in movies value.
# Decides how many times the Movie will be added to the final random list.
# Lottery number added if the adjAvg of the movie is >= the adjAvg for that rank. 
# This is so that ties will be considered at the higher group
for i in list(MovDictRanker.keys()):
    for j in range(stopper):
        if MovDictRanker[i][0] >= Ranker_values[rankgroup[j]-1]:
            MovDictRanker[i][1] += 1

# Create a list of movie names
# Names will be added n times
# N Depends on the second value in their dictionary entry
RandMovChose = []
for i in list(MovDictRanker.keys()):
	for j in range(MovDictRanker[i][1]):
		RandMovChose.append(i)

#print(RandMovChose)

# Randomly select movies from RandMovChose
# Put into dictionary in order, i.e. {1: "Goodfellas", 2: "Shaun of the Dead"}
# Remove all instances of movie
MovieOrderDict = {}
random.shuffle(RandMovChose)
movord = 1
for i in range(len(MovDictRanker)):
	a = random.randint(0,len(RandMovChose)-1)
	mov = RandMovChose[a]
	MovieOrderDict[movord] = mov
	movord += 1
	RandMovChose = list(filter(lambda a:  a!= mov, RandMovChose))

# Print order for easier copying
for i in range(1, len(MovieOrderDict)+1):
    print("Week", str(i)+":", MovieOrderDict[i])