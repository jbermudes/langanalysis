#! /usr/bin/env python3
import re

class Analyzer:

    def __init__(self, fname):
        self.filename = fname
        self.lines = []
        self.words = {}
        with open(self.filename) as file:
            lines = file.readlines()
            lines = [self.process_line(line) for line in lines]
        self.lines = lines

        for line in lines:
            self.count_words(line)

    def process_line(self, line):
        processed = line.strip()
        processed = re.sub('[",._?!@#$%&(){};:\[\]]', '', processed)
        processed = processed.lower()
        return processed

    def count_words(self, line):
        for word in line.split():
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1


    def tokenize():
        pass

if __name__ == "__main__":
    fname = "/home/jess/Learning English with The Simpsons/steamedhams_original.txt"
    analyzer = Analyzer(fname)
    print(len(analyzer.words))
    sorted_words = sorted(analyzer.words.items(), key=lambda x: x[1], reverse=True)
    for k,v in sorted_words:
        print(k + ", " + str(v))
