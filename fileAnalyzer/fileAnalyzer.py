with open("sample.txt","r") as file:
    text = file.read()
    lines = text.split("\n")
    words = text.split()
    num_lines = len(lines)
    num_words = len(words)
    num_chars = len(text)
    print(f"Number of lines is {num_lines}\n Number of words is {num_words}\n Number of characters is {num_chars}\n")
    freq = {} #dictionary
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    top_5 = sorted_words[:5]
    print("Top 5 most common words:")
    for word, count in top_5:
        print(f"{word}: {count}")
