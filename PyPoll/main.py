"""
The following script opens a csv file with election data and returns the following 
results: 1) The total number of votes cast. 2) A complete list of candidates who
received votes 3) The percentage of votes each candidate won 4) The total number of
votes each candidate won 4) The winner of the election based on popular vote

"""
# Import the necessary modules
import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Intialize these variables to 0
    total_votes = 0
    most_votes = 0
    other_person = 0

    # Create a dictionary for the candidates with last name as key and
    # value as the number of votes 
    candidates = {"Correy": 0, "Khan": 0, "Li":0, "O'Tooley":0}

    
    # Assign the first row in the file as the header
    header = next(csvreader)
    
    # Tally the votes for each candidate
    for row in csvreader:
      if row[2] == "Correy":
        candidates["Correy"] += 1
      elif row[2] == "Khan":
        candidates["Khan"] += 1
      elif row[2] == "Li":
        candidates["Li"] += 1
      elif row[2] == "O'Tooley":
        candidates["O'Tooley"] += 1
      else:
        # Should not occur - good for debugging
        other_person += 1

      # Tally all the votes in the election
      total_votes += 1
    # Used to avoid complications with the apostrophe in the print statement
    O_Tooley_votes = candidates["O'Tooley"]

    # Calculate percentage of total votes for each candidate
    Correy_perecent = candidates["Correy"] / total_votes
    Khan_percent = candidates["Khan"] / total_votes
    Li_percent = candidates["Li"] / total_votes
    O_Tooley_perecent = O_Tooley_votes / total_votes  

    # Determine which canditate received the most votes
    for k in candidates.keys():
      if candidates[k] > most_votes:
        most_votes = candidates[k]
        winner = k
      elif candidates[k] == most_votes:
        # Alert there is tie and something needs to be done to resolve
        print(f"There is a tie")

# Create and open the file poll_results and print results to file 
with open('poll_results.txt', 'w+', newline="") as file:
    file.write(f"Election Results\n")
    file.write(f"-------------------------\n")
    file.write(f"Total Votes:  {total_votes}\n")
    file.write(f"-------------------------\n")
    file.write(f"Khan: {Khan_percent:.3%} ({candidates['Khan']})\n")
    file.write(f"Correy: {Correy_perecent:.3%} ({candidates['Correy']})\n")
    file.write(f"Li: {Li_percent:.3%} ({candidates['Li']})\n")
    file.write(f"O\'Tooley: {O_Tooley_perecent:.3%} ({O_Tooley_votes})\n")
    file.write(f"-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write(f"-------------------------\n")
    
    # Go to the beginning of file and read & print to the terminal
    file.seek(0)
    print(file.read())

    
    





   

       




