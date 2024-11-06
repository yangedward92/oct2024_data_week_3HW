# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

filepath = "Resources/election_data.csv"



# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 300  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {"name A": 100, "name B": 200}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        pass
        #print(". ", end="")

winner = ""

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
for candidate_name in candidates.keys():
    output += f"{candidate_name}: {round(candidates.get(candidate_name)/total_votes,3)}% {candidates.get(candidate_name)}\n"
output += f""" 
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

