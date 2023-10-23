#Import required moudles
import csv
import os
import subprocess
# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the directory of your CSV file and set the path for the csv file.
os.chdir(current_dir)
csv_file_path = "Resources/election_data.csv"  # Path for CSV file

#Intialize the variables.
total_votes = 0 
winner = 0  
candidates_dict = {}  

# Open the CSV file for reading
with open(csv_file_path, 'r') as open_csv:
    csv_reader = csv.reader(open_csv) #Read the CSV file
    header = next(csv_reader)  # Store and Skip the header row

    # Loop through each row in the CSV file
    for column in csv_reader:
        total_votes += 1
        candidate = column[2]  # Candidate name column

        # Update the vote count for the candidate in the dictionary
        if candidate not in candidates_dict:
            candidates_dict[candidate] = 1
        else:
            candidates_dict[candidate] += 1

# Open a text file for writing the financial analysis
output_file_path = os.path.join(current_dir, 'analysis/Electionresults_analysis.txt')
with open(output_file_path, 'w') as output_file:
    # Print the election results
    print(f"Election Results")
    print(f"-----------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-----------------------")
    # Write the election results to the text file
    output_file.write("Election Results\n")
    output_file.write("-----------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-----------------------\n")

    # Loop through the candidates and calculate and write their vote percentages
    for candidate, vote_count in candidates_dict.items():
        vote_percentage = round((vote_count / total_votes) * 100, 3)
        print(f"{candidate}: {vote_percentage}% ({vote_count})")
        output_file.write(f"{candidate}: {vote_percentage}% ({vote_count})\n")

        # Check if the current candidate has more votes than the current winner
        if vote_count > winner:
            winner = vote_count
            winner_candidate = candidate
    # Print the winner of the election
    print(f"-----------------------")
    print(f"Winner: {winner_candidate}")
    print(f"-----------------------")
    # Write the winner of the election to the text file
    output_file.write("-----------------------\n")
    output_file.write(f"Winner: {winner_candidate}\n")
    output_file.write("-----------------------\n")

# Print a message to confirm that the results are saved
print("Election Results saved to Electionresults_analysis.txt")  
    