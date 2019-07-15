def count_words(filename):
    """Print count of each word in file.

    Prints each word in `filename` and the count of each word on separate lines.
    This function returns None.
    """

    file_data = open(filename)
    word_counts = {}

    for line in file_data:
        line = line.rstrip()        # Strip whitespace on the right.

        for word in line.split():   # Split line into words.
           word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():     # Unpacks key and value.
        print(word, count)


count_words("test.txt")
count_words("twain.txt")