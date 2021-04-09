import os
import csv

# Create a path
csv_path = os.path.join('Resources', 'election_data.csv')

total_votes = []
candidates_list = [] # list that will store the name of each candidate on the poll
candidates = []
votes = []
vote_count = {}
winner = "name"
listing_print = []


# Open file
with open(csv_path,'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skips header
    csv_header = next(csv_reader, None)
    for row in csv_reader:
        total_votes.append(row)                             # creates a list with element rows of the file
        candidates.append(row[2])                           # creates a list with with elements of the third column of the file
        votes.append(row[0])                                # creates a list with with elements of the first column of the file

candidates_list.append(candidates[0])                       # adds the first name of the "candidates" list to the "candidates_list" list

for i in range(1, len(candidates)):                         # loops through "candidates" list starting on second element
    if candidates[i] not in candidates_list:                # checks if the name(i) on the "candidates" list is not in the "candidates_list" list
        candidates_list.append(candidates[i])               # if the condition above us true, adds the name(i) of the "candidates" to the "candidates_list" list

for i in range(len(candidates_list)):                       # loops through the entire "candidates_list" list
    vote_count["votes_" + str(candidates_list[i])] = []     # creates a list for each candidate listed in the "candidates_list"
    for j in range(len(candidates)):                        # nested loop through the entire "candidates" list
        if candidates[j] == candidates_list[i]:             # compares each element of the "candidates" with each element of the "candidates_list"
            vote_count["votes_" + str(candidates_list[i])].append(votes[j])     # adds elements of the first column of the file to its correspondent candidate list

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(total_votes)))              # len of "total_votes" corresponds to total number of votes, which is printed in this line
print("-------------------------")

# for each candidate in the "candidates_list" list prints the name of the candidate, the percentage of votes for the candidate and the number of votes for the candidate
# the length of each "vote_count" list corresponds to the votes casted for the candidate that owns the list

for i in range(len(candidates_list)):
    print(candidates_list[i] + ":   " + str(round((len(vote_count["votes_" + str(candidates_list[i])]) / len(total_votes)) *100, 3)) + "%   (" + str(len(vote_count["votes_" + str(candidates_list[i])])) + ")")

winner = (candidates_list[0])                                  # initially associates the winner to the first element of the "candidates_list" list
for i in range(1,len(candidates_list)):                        # loops through the elements of the "candidates_list" from the second to the last element
    # tests if the percentage of votes of candidate i is greater than the percentage of votes of candidate i-1
    if ((len(vote_count["votes_" + str(candidates_list[i])]) / len(total_votes))) > ((len(vote_count["votes_" + str(candidates_list[i-1])]) / len(total_votes))):
        winner = (candidates_list[i])                          # if statement above is true, attributes the winner to candidate i.

print("-------------------------")
print("Winner:  " + winner)


elem1 = "Election Results"
elem2 = "-------------------------"
elem3 = "Total Votes: " + str(len(total_votes))
elem4 = "-------------------------"
for i in range(len(candidates_list)):
    listing_print.append(candidates_list[i] + ":   " + str(round((len(vote_count["votes_" + str(candidates_list[i])]) / len(total_votes)) *100, 3)) + "%   (" + str(len(vote_count["votes_" + str(candidates_list[i])])) + ")")
elem5 = "-------------------------"
elem6 = "Winner:  " + winner

# creates lists of characters related to the printed lines above

textList = [elem1,elem2,elem3,elem4]
textList1 = [elem5, elem6]

os.mkdir('Analysis')                                                # created the "Analysis" directory
output_path = os.path.join('Analysis', 'analysis_results.txt')      # creates the path where the output file will be written
out = open(output_path, 'w', newline="")                            # creates and opens the output file

# writes results to the output file

for line in textList:
    out.write(line)
    out.write("\n")

for line in listing_print:
    out.write(str(line)+'\n')

for line in textList1:
    out.write(line)
    out.write("\n")

# closes the file
out.close()