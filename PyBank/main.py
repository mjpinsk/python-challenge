"""
The following script opens a csv file with bank data and returns the following 
results: 1) The total number of months included in the dataset 2) The net total 
amount of "Profit/Losses" over the entire period 3) The average of the changes in
"Profit/Losses" over the entire period 4) The greatest increase in profits 
(date and amount) over the entire period 5) The greatest decrease in losses
(date and amount) over the entire period

"""
# Import the necessary modules
import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('Resources', 'budget_data.csv')


# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize these variables
    num_months = 0
    current_profit = 0
    greatest_increase = 0
    greatest_decrease = 0
    total_profit = 0
    worst_month = "month"
    difference = []

    # Assign the first row in the file as the header
    header = next(csvreader)    
   
    # Iterate to the end of the file performing some simple comparisons
    # and calculations
    for row in csvreader:
      # Caculate the change in profit from month to month
      change_profit = int(row[1]) - current_profit
      # Create a list of month to month differences
      difference.append(change_profit)
      # Determine the month and corresponding amount with greatest increase and decrease
      if change_profit > greatest_increase and change_profit != difference[0]:
        greatest_increase = change_profit
        greatest_month = row[0]
      elif change_profit < greatest_decrease and change_profit != difference[0]:
        greatest_decrease = change_profit
        worst_month = row[0]

      # Update the current profit of the corresponding month
      current_profit = int(row[1])
      # Calculate the total profit of all the months
      total_profit = total_profit + int(row[1])
      # Calculate the total number of months
      num_months += 1
      
    # Remove the first month from difference (change_profit) list
    # which is just the first month profit
    difference.remove(difference[0])
    # Caluculate the average of the changes in "Profit/Losses"
    # Note the total numer of changes is one less than the total number of months
    average_change = sum(difference) / (num_months - 1) 
   
# Create and open the file poll_results and print results to file 
with open('financial_analysis.txt', 'w+', newline="") as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {num_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})\n")

    # Go to the beginning of file and read & print to the terminal
    file.seek(0)
    print(file.read())






   

       




