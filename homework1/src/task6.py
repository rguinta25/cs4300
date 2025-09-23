def count_words(file_name):
    """
    Count the number of words in .txt file

    Parameters:
        file_name: path to .txt file

    Returns:
        Number of words in file
    """
    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

    file.close()
    return word_count

if __name__ == "__main__":
    print("The amount of words in the file is: ", count_words("task6_read_me.txt"))
