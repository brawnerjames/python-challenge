import os
import csv

csvpath = os.path.join("election_data.csv")
text_output = os.path.join('budget_analysis.txt')

vote_count = 0

Khan_count = 0
Li_count = 0
Correy_count = 0
OTooley_count = 0
candidate_list = []
cand_count = 0
total_vote_list = []

with open(csvpath, newline ="") as csvfile:
    election_csv = csv.reader(csvfile, delimiter = ",")

    poll_header = next(election_csv)

    for row in election_csv:
        
        vote_count = vote_count + 1

        if row[2] == "Khan":
            Khan_count = Khan_count + 1
        elif row[2] == "Li":
            Li_count = Li_count + 1
        elif row[2] == "Correy":
            Correy_count = Correy_count + 1
        elif row[2] == "O'Tooley":
            OTooley_count = OTooley_count + 1
        
        if row[2] in candidate_list:
            cand_count = cand_count
        elif row[2] not in candidate_list:
            cand_count = cand_count + 1
            candidate_list.append(row[2])
    

khan_percent = "%.0f%%" % ((Khan_count/vote_count)*100)
li_percent = "%.0f%%" % ((Li_count/vote_count)*100)
correy_percent = "%.0f%%" % ((Correy_count/vote_count)*100)
otooley_percent = "%.0f%%" % ((OTooley_count/vote_count)*100)

total_vote_dict = {
    candidate_list[0]:Khan_count,
    candidate_list[2]:Li_count,
    candidate_list[1]:Correy_count,
    candidate_list[3]:OTooley_count
}

winner_num = 0

for key,value in total_vote_dict.items():
    if value < winner_num:
        winner = winner
    elif value > winner_num:
        winner_num = value
        winner = key


output = (
f"\nElection Results\n"
f"----------------------------\n"
f"Total Votes: {vote_count}\n"
f"----------------------------\n"
f"{candidate_list[0]}: {khan_percent} ({Khan_count})\n"
f"{candidate_list[2]}: {li_percent} ({Li_count})\n"
f"{candidate_list[1]}: {correy_percent} ({Correy_count})\n"
f"{candidate_list[3]}: {otooley_percent} ({OTooley_count})\n"
f"Winner: {winner}\n"
)

print(output)

with open(text_output, "w") as txt:
    txt.write(output)