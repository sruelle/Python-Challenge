#Dependencies
import pandas as pd

#name of the csv file
election_file = 'election_data2.csv'



#Use Pandas to read data
election_file_pd =pd.read_csv(election_file)
election_file_pd.head()

# The sum method adds every entry in the series
total = election_file_pd["Voter Id"].sum()
total

# the unique method shows every element of the series that appears only once
unique = election_file_pd["Canidadate"].unique()
unique

# the value_counts method counts the uniques values in a column
count = election_file_pd["Candidate"].value_counts()
count



