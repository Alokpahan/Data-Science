# poem.txt contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in your python program and find out words with maximum occurance.

# Initialize an empty dictionary to store word statistics.
word_stats = {}

# Open the "poem.txt" file in read mode.
with open("poem.txt", "r") as f:
    # Loop through each line in the file.
    for line in f:
        # Split the line into a list of words using ',' as the delimiter.
        words = line.split(',')
        print(words)  # Print the list of words for debugging purposes.

        # Loop through each word in the list.
        for word in words:
            # Check if the word is already in the word_stats dictionary.
            if word in word_stats:
                # If it's already in the dictionary, increment its count.
                word_stats[word] += 1
            else:
                # If it's not in the dictionary, add it with a count of 1.
                word_stats[word] = 1

# Print the word statistics dictionary.
print(word_stats)

# Create a list of word occurrences by extracting the values from the word_stats dictionary.
word_occurrences = list(word_stats.values())

# Print the list of word occurrences.
print(word_occurrences)

# Find the maximum occurrence count in the list.
max_count = max(word_occurrences)

# Print the maximum occurrence count.
print("Max occurrences of any word is:", max_count)

# Print words with the maximum occurrences.
print("Words with max occurrences are:")
for word, count in word_stats.items():
    if count == max_count:
        print(word)
