#Dependencies
import pandas as pd


#name the file
election_file =("../Resources/election_data.csv")

#Use Pandas to read data
election_file_pd = pd.read_csv(election_file)
#print (election_file_pd)
##Print(dataframename.head())

#Counts the number of votes made total
count = election_file_pd["Voter ID"].value_counts()
total = count.sum()

# the unique method shows every element of the series that appears only once
unique = election_file_pd["Candidate"].unique()
#print (unique)

# the value_counts method counts the uniques values in a column
count = election_file_pd["Candidate"].value_counts()


# the percentage of votes per candidate
#percentage_of_votes = election_file_pd("count"//"total")
#print(percentage_of_votes)




#print results
print("Election Results")       
print("----------------")
print(f"Total Votes: {total}")
print("----------------")
print (count)
#print("---------------- \n")
#for i in range(len(candidates)):
    #print(f"{candidateData[i]}")
#print("----------------")
#print(f"Winner: {winningCandidate}")



