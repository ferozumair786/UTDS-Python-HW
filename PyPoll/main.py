import os
import csv
import timeit

#import file
polling = os.path.join("election_data.csv")

#set variables
votes = []
candidates = []
total = []
percent_vote = []
total_votes = 0
winner = str(0)



#open file
with open(polling,newline="") as pollfile:
    pollreader = csv.reader(pollfile,delimiter=",")
    header = next(pollreader)

    #loop through each row in file
    for row in pollreader:
        votes.append(row[2])
        total_votes = total_votes + 1

        if row[2] not in candidates:
            candidates.append(row[2])

    for candidate in candidates:
        votesum = 0
        percentage = 0

        for vote in votes:
            if vote == candidate:
                votesum = votesum + 1
        total.append(votesum)
        percentage = round((votesum / total_votes)*100, 2)
        percent_vote.append(percentage)
        #print(votesum)
        #print(max(total))
        if votesum == max(total):
            winner = candidate

    print("Election Results\n-------------------------------------")
    print(f"Total Votes: {total_votes}\n-------------------------------------")
    
    for candidate, pcent, numbers in zip(candidates, percent_vote, total):
        print(f"{candidate}: {pcent}% ({numbers})")
    print("-------------------------------------")
    print(f"Winner: {winner}\n-------------------------------------")



    with open('poll_results.csv', 'w', newline='') as resultfile:
        resultwriter = csv.writer(resultfile, delimiter = ',')
        resultwriter.writer(candidates)