"""
The solution must be a python script with command line interface. Script input is a text file and the output is statistics of word occurrences. 
As a result, the program must print out all unique words from the text with the number of their occurrences. 
Words in output must be sorted by number of their occurrences in descending order, words with the equal number of occurrences must be sorted in alphabetic order. 
Each word and number of its occurrences must be printed on a new line in format: <word>: <frequency>.
"""

from sys import argv
from collections import Counter


def read_file(filename):
    with open(filename, 'r') as f:
        return Counter(f.read().lower().split())


def main():

    if len(argv) != 2 :
        print("Usage: python " + argv[0] + " filename")
        return 1

    wordDict = read_file(argv[1])
    for k, v in sorted(wordDict.items(), key=lambda x: (-x[1],x[0])):
        print("%s: %s" % (k,v))


if __name__ == "__main__":
    main()
