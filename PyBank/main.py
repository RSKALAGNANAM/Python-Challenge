# Python Home Work
# In this assignment we will:
# Read the file /Resources/budget_data.csv to get the following:
# 1. Total number of months included in the dataset (i.e., count of records excl. Header)
# 2. Net Total Amount of Profit/Losses over the entire period
# 3. Average of the changes over the entire period
# 4. Greatest increase in profits (date and amount) over the entire period
# 5. Greatest decrease in losses (date and amount) over the entire period

# Import the "os", "csv" and "sys" modules
import os
import csv

# At the very outset I am defining a function so that I can
# format the $ values to be displayed with "comma" separators for "1000s"
# I found this funcation at at
# https://www.geeksforgeeks.org/print-number-commas-1000-separators-python/

def place_value(number): 
    return ("{:,}".format(number)) 

# Define the path to read the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read the file using ',' as the delimiter

with open(csvpath,newline='') as csvfile:
    #specify the delimiter
    csvreader = csv.reader(csvfile,delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read the first line of Data
    # This is important because we want to save the first line for
    # calculating the "differences" change in P/L after month 2 =
    # P/L at the end of month 2 MINUS P/L at the end of month 1

    first_row = next(csvreader)
    PL_Previous = int(first_row[1])
        

    # The following code will count the number of months and
    # estimate the sum of the profit and loss

    # Set variable 'month_count' to keep a count of the Rows
    # following the header as well as the first Row and 
    # initialize to '1' because we are now on Row 1

    month_count = 1

    # Set a variable 'total_PL' to keep the sum of the monthly
    # profit and loss and set it to the value of the first Rows's
    # Profit/Loss

    total_PL = PL_Previous
    total_PL_Diff = 0

    # Set two variables max_diff and min_diff and initialize them 
    # to "0"

    max_diff = 0
    min_diff = 0

    # Read each row of data after the header
    # to get the number of months and Total Profit/Loss
    for row in csvreader:
        month_count = month_count+1
        PL_Current=int(row[1])
        total_PL = total_PL + int(row[1])
        PL_diff = PL_Current - PL_Previous
        total_PL_Diff = total_PL_Diff+PL_diff
        if PL_diff > max_diff:
            max_diff = PL_diff
            month_max_diff = str(row[0])
        if PL_diff < min_diff:
            min_diff = PL_diff
            month_min_diff = str(row[0])
        PL_Previous = PL_Current

    # Calculate the average change (total_PL/month_count)

    average_PL_Diff = round(total_PL_Diff/(month_count-1),2)

    # Adjust all $ values to show comma separators

    adj_total_PL = place_value(total_PL)
    adj_max_diff = place_value(max_diff)
    adj_min_diff = place_value(min_diff)
    adj_avg_PL_Diff = place_value(average_PL_Diff)

    # Write the results to the Screen

    # Print a blank line to separate the output from whatever is currently on the screen

    print("")

    # Print a line to indicate beginning of output

    print("--------------------------------------------------------")

    # Print another blank line

    print("")

    # Print the header, "Financial Analysis"

    print("FINANCIAL ANALYSIS")

    # Print another blank line

    print("")

    # Print a line to indicate beginning of output summary

    print("--------------------------------------------------------")

    print("Total number of Months: " + str(month_count))
    print("Total Profit/Loss: " + "$" + str(adj_total_PL))
    print("Average Change: " + "$" + str(adj_avg_PL_Diff))
    print("Greatest Increase in Profits: " + month_max_diff + " "
           + "$" + str(adj_max_diff))
    print("Greatest Decrease in Profits: " + month_min_diff + " "
           + "$" + str(adj_min_diff))

    # Print another blank line

    print("")

    # Print a line to indicate end of output summary

    print("--------------------------------------------------------")


    # Write the results to a file "PyBankResults.txt"

    # Specify the path to write to a text file
    file_to_write = open("PyBankResults.txt","w")

    # Print a blank line to separate the output from whatever is currently on the screen

    file_to_write.write(" \n")

    # Print a line to indicate beginning of output

    file_to_write.write("-------------------------------------------------------- \n")

    # Print another blank line

    file_to_write.write(" \n")

    # Print the header, "Financial Analysis"

    file_to_write.write("FINANCIAL ANALYSIS \n")

    # Print another blank line

    file_to_write.write(" \n")

    # Print a line to indicate beginning of output summary

    file_to_write.write("-------------------------------------------------------- \n")

    file_to_write.write("Total number of Months: " + str(month_count) + "\n")
    file_to_write.write("Total Profit/Loss: " + "$" + str(adj_total_PL) + "\n")
    file_to_write.write("Average Change: " + "$" + str(adj_avg_PL_Diff) + "\n")
    file_to_write.write("Greatest Increase in Profits: " + month_max_diff + " "
           + "$" + str(adj_max_diff) + "\n")
    file_to_write.write("Greatest Decrease in Profits: " + month_min_diff + " "
           + "$" + str(adj_min_diff) + "\n")

    # Print another blank line

    file_to_write.write(" \n")

    # Print a line to indicate end of output summary

    file_to_write.write("-------------------------------------------------------- \n")

    file_to_write.close()

    # Print another blank line

    print("")

    print("Completed writing to output file.")