# Import the required module 
import csv
import os
import subprocess  

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the directory of your CSV file and set the path of the file.
os.chdir(current_dir)
csv_file_path = 'Resources/budget_data.csv'

# Initialize variables to store financial data
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""
profit_loss_changes = []

# Open and read the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file) #Reads CSV file
    header = next(csv_reader)  # Store and skip the header row
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total months
        total_months += 1
        
        # Calculate total profit/loss
        total_profit_loss += profit_loss
        
        # Calculate profit/loss change
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
        
        # Update previous_profit_loss for the next iteration
        previous_profit_loss = profit_loss    
        
        # Find the greatest increase and decrease
        if profit_loss_change > greatest_increase:
            greatest_increase = profit_loss_change
            greatest_increase_month = date
        if profit_loss_change < greatest_decrease:
            greatest_decrease = profit_loss_change
            greatest_decrease_month = date
        
# Calculate the average change
average_change = sum(profit_loss_changes) / (total_months - 1)

#Open a text file for writing the financial analysis
output_file_path = os.path.join(current_dir, 'analysis/Financial_analysis.txt')
with open(output_file_path, 'w') as output_file:
   # Print the financial analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
    # Write the financial analysis to the text file
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
# Print a message to confirm that the results are saved
print("Financial analysis saved to financial_analysis.txt")