import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Read in Election csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read Election csv header
    csv_header = next(csvreader)
    
    # Set variables, lists
    total_votes = 0
    loop_count = 0
    candidate_vote_count = 0
    candidates = []
    unique_candidates = []
    vote_counts = []
    vote_percentages = []
    strings = []

    for row in csvreader:    

        # Calculate the total number of votes cast
        total_votes += 1 

        # Create a list containing all values in the candidate column
        candidates.append(row[2])

    # Calculate a complete (unique) list of candidates who received votes (https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python)
    for candidate in candidates:
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)

    # Calculate the total number and percentage of votes each candidate won
    while loop_count < len(unique_candidates):
        for candidate in candidates:
            if unique_candidates[loop_count] == candidate:
                candidate_vote_count += 1
        vote_counts.append(candidate_vote_count)
        vote_percentage = round((candidate_vote_count / total_votes) * 100, 3)
        vote_percentages.append(vote_percentage)
        string = f"{unique_candidates[loop_count]}: {vote_percentage}% ({candidate_vote_count})"
        strings.append(string)    
            
        # Next loop/candidate
        loop_count += 1
        # Reset count
        candidate_vote_count = 0

    # Calculate the winner of the election based on popular vote
    winner_index = vote_counts.index(max(vote_counts))
    winner = unique_candidates[winner_index]

    # Display results
    print('Election Results')
    print('--------------------------------')
    print(f"Total Votes: {total_votes}")
    print('--------------------------------')
    for string in strings:
        print(string)
    print('--------------------------------')
    print(f"Winner: {winner}")
    print('--------------------------------')

    # Export results to text file (https://www.pythontutorial.net/python-basics/python-write-text-file/)    
    with open('../Analysis/election_results.txt', 'w') as txt_file:
        txt_file.write('Election Results\n')
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Total Votes: {total_votes}\n")
        txt_file.write('--------------------------------\n')
        for string in strings:
            txt_file.write(f"{string}\n")
        txt_file.write('--------------------------------\n')
        txt_file.write(f"Winner: {winner}\n")
        txt_file.write('--------------------------------')
