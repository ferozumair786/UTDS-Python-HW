import os
import csv

#import file
polling = os.path.join("election_data.csv")

#set variables
votes = []
candidates = []
total = []


#open file
with open(polling,newline="") as pollfile:
    pollreader = csv.reader(pollfile,delimiter=",")
    header = next(pollreader)

    #loop through each row in file
    for row in pollreader:
        votes.append(row[2])

        if row[2] not in candidates:
            candidates.append(row[2])

    for candidate in candidates:
        votesum = 0

        for vote in votes:
            if vote == candidate:
                votesum = votesum + 1
        total.append(votesum)
    print(total)

    #print(votes)
    #print(candidates)
    #print(total)