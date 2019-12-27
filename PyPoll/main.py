#Import objects
import os
import csv

#Set the path for the csv file
file_path = os.path.join('..', 'Resources', 'election_data.csv')

#Initiate dicitionary
votes=[]
candidates=[]

#Initiate variables
winning_votes = 0
winner = ''

#Created function to calculate the total votes for a given candidate and to return that total
def calculate_votes(candidate_name,total_votes):

    #Initiate variables
    i=0
    total_candidate_votes = 0
    percent_of_votes = 0

    #Loop through the votes list to add the votes for the given candidate
    while i < len(votes):

        if votes[i] == candidate_name:
            total_candidate_votes += 1

        i += 1

    #Calcualte the percentage of votes for the given candidate
    percent_of_votes = round(((total_candidate_votes/total_votes) * 100),3)

    #display the candidates information on the terminal
    print(f' {candidate_name}: {percent_of_votes:.3f}% ({total_candidate_votes})')

    #Write the candidates information to the text file
    Election_File.write(f' {candidate_name}: {percent_of_votes:.3f}% ({total_candidate_votes}) \n')

    return total_candidate_votes

#Open and read csv file
with open(file_path,newline="",encoding="utf8") as elect_data:
    elect_data_read = csv.reader(elect_data,delimiter=',')

    #Skip the header
    elect_header = next(elect_data_read)

    #Create lists for each row and determine the total votes
    votes = [row[2] for row in elect_data_read]
    total_votes = len(votes)

    #Display the total votes on the terminal
    print(f'--- text')
    print(f'Election Results')
    print(f'-----------------------')
    print(f'Total Votes: {total_votes}')
    print(f'-----------------------')

    #Write the total votes to a text file
    Election_File = open('Election.txt','a')
    Election_File.write('---text \n')
    Election_File.write('Election Results \n')
    Election_File.write('------------------------ \n')
    Election_File.write(f'Total Votes: {total_votes} \n')
    Election_File.write('------------------------ \n')

    #Loop through the votes to get the separate candidate names and call the function to calculate their votes
    for candidate_name in votes:

        if candidate_name not in candidates:
            candidates.append(candidate_name)
            total_candidate_votes = calculate_votes(candidate_name,total_votes)

        #Use the returned candidate votes to determine the winner
        if winning_votes < total_candidate_votes:
            winning_votes = total_candidate_votes
            winner = candidate_name

#Display the winner on the terminal
print(f'-----------------------')
print(f'Winner: {winner}')
print(f'-----------------------')
print(f'--')

#Write the winner to the text file
Election_File.write('------------------------ \n')
Election_File.write(f'Winner: {winner} \n')
Election_File.write('------------------------ \n')
Election_File.write('--- \n')

Election_File.close()
