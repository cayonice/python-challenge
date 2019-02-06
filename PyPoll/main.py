import csv

poll_csv='C:\\UKED201811DATA5\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv'

total_votes=0
candidates=[]
vote_count={}


with open(poll_csv,"r") as poll:
    csvreader=csv.DictReader(poll)

    for row in csvreader:
    	total_votes +=1
    	if row ['Candidate'] not in candidates:
    		candidates.append(row['Candidate'])
    		vote_count[row['Candidate']]=1
    	elif row ['Candidate']	in candidates:
    		vote_count[row['Candidate']] += 1

prev_cand= 0

print("Election Results")
print("Total Vote Counts: "+ str(total_votes))
for key, value in vote_count.items():
    print(key+": "+ str(round((float(value/total_votes)*100),1))+"%"+" ("+ str(value)+")")
for key, value in vote_count.items():
    if value > prev_cand:
        most_vote = key
        prev_cand = value
print("-------------------------")
print("Winner: " + most_vote)
print("-------------------------")
