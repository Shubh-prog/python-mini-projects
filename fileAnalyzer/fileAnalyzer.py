#Open the text file in read only mode
with open("sample.txt","r") as file:
    #Read the entire content of the file
    text = file.read()
    #Split the text into lines
    lines = text.split("\n")
    #Split the text into words
    words = text.split()
    #Count the number of lines, words, and characters
    num_lines = len(lines)
    num_words = len(words)
    num_chars = len(text)
    #Print basic statistics
    print(f"Number of lines is {num_lines}\n Number of words is {num_words}\n Number of characters is {num_chars}\n")
    #Initialize a dictionary to store word frequencies
    freq = {}
    #Count the frequency of each word
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    #Sort the dictionary items by frequency in descending order
    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    #Get the top 5 common words
    top_5 = sorted_words[:5]
    print("Top 5 most common words:")
    #Print the 5 most common words
    for word, count in top_5:
        print(f"{word}: {count}")
