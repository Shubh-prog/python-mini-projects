# Text Analysis in Python

A simple Python program that analyzes a text file and provides basic statistics and word frequency information.

## Features

- Counts the number of lines, words, and characters in a text file.
- Calculates the frequency of each word in the text.
- Displays the **top 5 most common words** along with their counts.

## How It Works

1. Reads a text file (`sample.txt`) from the current directory.
2. Splits the text into lines and words.
3. Counts:
   - Total lines
   - Total words
   - Total characters
4. Uses a dictionary to store word frequencies.
5. Sorts the words by frequency and displays the top 5.

## Example Output

Number of lines is 10
Number of words is 50
Number of characters is 300

Top 5 most common words:
the: 7
and: 5
Python: 4
file: 3
text: 3

## How to Run

1. Make sure you have Python 3 installed.
2. Place your text file in the same directory as the script and name it `sample.txt`.
3. Run the script:

```bash
python text_analysis.py
