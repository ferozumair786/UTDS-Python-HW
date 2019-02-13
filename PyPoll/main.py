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
        
        #copy votes to list and calculate total votes
        votes.append(row[2])
        total_votes = total_votes + 1

        #copy the unique list of candidates into a new list
        if row[2] not in candidates:
            candidates.append(row[2])

    #loop through candidates list to operate one candidate at a time
    for candidate in candidates:
        
        #reset variables to zero after it loops through each candidate
        votesum = 0
        percentage = 0

        #loop through the votes list for each candidate
        for vote in votes:
            
            #calculate total votes per candidate
            if vote == candidate:
                votesum = votesum + 1
        
        #in the same loop, add the total votes for each candidate into a new list
        total.append(votesum)
        
        #calculate and add percentage votes into a new list
        percentage = round((votesum / total_votes)*100, 2)
        percent_vote.append(percentage)
        
        #figure out who is the winner
        if votesum == max(total):
            winner = candidate

    #saving space with print statements
    print("Election Results\n-------------------------------------")
    print(f"Total Votes: {total_votes}\n-------------------------------------")
    
    #loop through all the lists and print the relevant values
    for candidate, pcent, numbers in zip(candidates, percent_vote, total):
        print(f"{candidate}: {pcent}% ({numbers})")
    
    print("-------------------------------------")
    print(f"Winner: {winner}\n-------------------------------------")


    #print things to a txt file so things look good
    with open('poll_results.txt', 'w') as resultfile:
        resultfile.write("Election Results\n")
        resultfile.write("-------------------------------------\n")
        resultfile.write(f"Total Votes: {total_votes}\n")
        for candidate, pcent, numbers in zip(candidates, percent_vote, total):
            resultfile.write(f"{candidate}: {pcent}% ({numbers})\n")
        resultfile.write("-------------------------------------\n")
        resultfile.write(f"Winner: {winner}\n-------------------------------------\n")
       