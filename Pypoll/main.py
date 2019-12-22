#Dependencies
import pandas as pd


#name the file
election_file =("../Resources/election_data2.csv")

#Use Pandas to read data
election_file_pd = pd.read_csv(election_file)
print (election_file_pd)
#Print(dataframename.head())

#Counts the number of votes made
count = election_file_pd["Voter ID"].value_counts()
total = count.sum()
print (total)

# the unique method shows every element of the series that appears only once
unique = election_file_pd["Candidate"].unique()
print (unique)

# the value_counts method counts the uniques values in a column
count = election_file_pd["Candidate"].value_counts()
print (count)




