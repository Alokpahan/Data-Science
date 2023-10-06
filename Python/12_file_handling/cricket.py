# Create an empty dictionary to store player scores
player_scores = {}

# Open the "scores.csv" file in read mode using a 'with' statement
with open("scores.csv", "r") as f:
    # Iterate through each line in the file
    for line in f:
        # Split each line into tokens using a comma as the delimiter
        tokens = line.split(',')

        # Extract the player name (the first token)
        player = tokens[0]

        # Extract the score (the second token) and convert it to an integer
        score = int(tokens[1])

        # Check if the player is already in the dictionary
        if player in player_scores:
            # If the player is in the dictionary, append the score to their list of scores
            player_scores[player].append(score)
        else:
            # If the player is not in the dictionary, create a new entry with their name as the key
            # and a list containing their score as the value
            player_scores[player] = [score]

# Print the dictionary containing player scores
print(player_scores)

# Iterate through the dictionary to find and print the minimum and maximum scores for each player
for player, score_list in player_scores.items():
    min_score = min(score_list)
    max_score = max(score_list)
    print(f'{player} ==> min:{min_score} max:{max_score}')


