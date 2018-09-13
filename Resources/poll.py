
import os
import csv


voter_id = []
county = []
voting_data = {}
count = 0
candidates = []
vote_count = [] 



file = os.path.join("election_data.csv")
with open(file, newline = "") as csvfile :
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
    
    for row in csvreader :
        voter_id.append(row[0])
        candidates.append(row[2])
        voting_data[row[0]]=row[2]

total_votes = len(voter_id)


individual_candidate = list(set(candidates))
# vote count for each candidate
for i in range (len(individual_candidate)):
    for values in voting_data.values() :
        if values == individual_candidate[i]:
            count += 1
    vote_count.append(count)
    count = 0
max_vote_index = vote_count.index(max(vote_count))

output_file = os.path.join('newpolloutput.txt') 
with open(output_file, 'w', newline ="") as datafile: 
    writer  = csv.writer(datafile)
    writer.writerow(['-----------------------------------------------------------'])
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------------------------------"])
   # * The total number of votes cast 
    writer.writerow(["Total Votes: " + str(total_votes)])
    writer.writerow(["-------------------------------------------------"])
    # * A complete list of candidates who received votes
    for i in range (len(individual_candidate)):
        writer.writerow([individual_candidate[i] +": "+ str((vote_count[i]/total_votes)*100) +"%  (" + str(vote_count[i]) +")"])
    writer.writerow(["-------------------------------------------------"])
    # * The winner of the election based on popular vote.
    writer.writerow(["Winner: " + str(individual_candidate[max_vote_index])])
    writer.writerow(["-------------------------------------------------"])
    
with open(output_file, 'r', newline="")as datafile :
    reader = csv.reader(datafile, delimiter = ",")
    for row in reader:
        print(row)