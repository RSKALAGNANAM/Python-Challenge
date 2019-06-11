# Python Home Work
# In this assignment we will:
# Read the file /Resources/election_data.csv to get the following:
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote
# Import the "os" and "csv" modules
import os
import csv

# At the very outset I am defining a function so that I can
# format the $ values to be displayed with "comma" separators for "1000s"
# I found this funcation at at
# https://www.geeksforgeeks.org/print-number-commas-1000-separators-python/

def place_value(number): 
    return ("{:,}".format(number))

# Define the path to the csv file
csvpath = os.path.join('Resources', 'election_data.csv')
#csvpath = os.path.join('election_data.csv')

# Read the file using ',' as the delimiter

with open(csvpath,newline='') as csvfile:
    #specify the delimiter
    csvreader = csv.reader(csvfile,delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

# Define variables "total_votes" and initialize to zero
    total_votes = 0

# Define a dictionary "votes" to store the names and 
# number of occurrences (votes)

    votes = {}

    # Define a list "final_list" to store the names and 
    # number of occurrences (votes)

    final_list = []

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in votes:
            votes[row[2]] = 0
        votes[row[2]] = votes[row[2]] + 1

    total_votes_adj = place_value(total_votes)

    final_list = [{'Name' : elem, 'Votes': int(votes[elem])} for elem in votes]

    final_list_adj = [{'Name' : elem, 'Votes': place_value(int(votes[elem])), 
                 'votepercent': int((votes[elem]/total_votes)*100)} for elem in votes]

    #Print a line at the top to indicate beginning of output

    print("---------------------------------------------------------")

    #Print a blank line

    print("")

    #Print header "Election Results"

    print("Election Results")

    #Print a blank line

    print("")

    #Print a line separating the header

    print("---------------------------------------------------------")

    #Print a blank line

    print("")
    
    print("Total number of votes cast: " + str(total_votes_adj))

    #Print a blank line

    print("")

    #Print a line separating the total vote count

    print("---------------------------------------------------------")

    #Print a blank line

    print("")   
    
    #print(final_list) - I used this while testing my code

    #print(final_list_adj) - I used this while testing my code

    # Print the final vote tally for each candidate

    for i in final_list_adj:
        print("Candidate: "+ str(i['Name']) + "; Votes Received: " + str(i['Votes']) + "; Vote Share: " + str(i['votepercent']) + " percent")

    #Print a blank line

    print("")

    #Print a line separating the individual results

    print("---------------------------------------------------------")

    #Print a blank line

    print("")

    #Process the list final_list_adj to identify the winner based on
    # percent votes received       

    # Define variable election_winner which will be used to identify the winner
    election_winner = ""

    # Define variable final_vote_percent and initialize to 0
    final_vote_percent = 0

    for i in final_list_adj:
        if int(i['votepercent']) > final_vote_percent:
            final_vote_percent = int(i['votepercent'])
            election_winner = i['Name']

    print("Winner is: " + str(election_winner) + " with " + 
          str(final_vote_percent) + " percent of the votes")

    #Print a blank line

    print("")
    
    #Print a line at the top to indicate end of output

    print("---------------------------------------------------------")

    # Write the results to a file "PyElectionResults.txt"

    # Specify the path to write to a text file
    file_to_write = open("PyElectionResults.txt","w")

    print("Writing results to output file.")

    # Print a blank line to separate the output from whatever is currently on the screen

    file_to_write.write(" \n")

    # Print a line to indicate beginning of output

    file_to_write.write("-------------------------------------------------------- \n")

    # Print another blank line

    file_to_write.write(" \n")

    # Print the header, "Election Analysis"

    file_to_write.write("ELECTION RESULT ANALYSIS \n")

    # Print another blank line

    file_to_write.write(" \n")

    file_to_write.write("Total number of votes cast: " + str(total_votes_adj))

    # Print another blank line

    file_to_write.write(" \n")

    # Print a line to indicate beginning of output summary

    file_to_write.write("-------------------------------------------------------- \n")

    for i in final_list_adj:
        file_to_write.write("Candidate: "+ str(i['Name']) + "; Votes Received: " + str(i['Votes']) + "; Vote Share: " + str(i['votepercent']) + " percent" + " \n")

    #Print a blank line

    file_to_write.write(" \n")

    #Print a line separating the individual results

    file_to_write.write("--------------------------------------------------------- \n")

    #Print a blank line

    file_to_write.write(" \n")

    #Print a blank line

    file_to_write.write("Winner is: " + str(election_winner) + " with " + 
          str(final_vote_percent) + " percent of the votes" + " \n")

    #Print a blank line

    file_to_write.write(" \n")
    
    #Print a line at the bottom to indicate end of output

    file_to_write.write("--------------------------------------------------------- \n")

    file_to_write.close()

    # Print another blank line

    print("")

    print("Completed writing to output file.")