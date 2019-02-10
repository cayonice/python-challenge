import os
import csv

candidates = []
votes = 0
vote_counts = []
election_data = ['1', '2']

#Data path is to election data
election_dataCSV = csvpath = os.path.join("election_data.csv")
#Reading csv file 
with open(election_dataCSV) as csvfile:
       csvreader = csv.reader(csvfile, delimiter=',')
       line = next(csvreader,None)

#loop through file
       for line in csvreader:        
            votes = votes +1
            candidate = line[2]
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1

            else:
                candidates.append(candidate)
                vote_counts.append(1)
   
percentages = []
max_votes = vote_counts[0]
max_index = 0

#Set secong loop an dcalulate result values    
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#Calculate percentage values
percentages = [round(i,2) for i in percentages]

#Print results on terminal 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
print("--------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("--------------------------")
print(f"Winner:  {winner}")
print("--------------------------")

#Set output text file
output_file =os.path.join("poll.txt")
write_data = f"{output_file}"
writer = open(write_data, mode = 'w')

# Write results to text file
writer.write("Election Results\n")
writer.write("-----------------------------\n")
writer.write(f"Total Votes:  {votes}\n")
writer.write("-----------------------------\n")
for count in range(len(candidates)):
    writer.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
writer.write("-----------------------------\n")
writer.write(f"Winner:  {winner}\n")
writer.write("-----------------------------\n")

# Close the text file
writer.close()