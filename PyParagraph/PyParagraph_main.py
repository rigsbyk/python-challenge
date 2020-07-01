#!/usr/bin/env python
# coding: utf-8

# Import os
# Import re to do regular expressions
import os
import re


# Open paragraph_1.txt and read it
f = open('Resources/paragraph_1.txt', 'r')
lines = f.read()

# Finding the approximate word count
words = re.sub("[\-,><,(),\–,\.]",'',lines).replace('','')
wordsplit = re.split(' ',words)
wordcount = len(wordsplit)

# Finding the approximate sentence count
sentences = re.sub("[\n]",'',lines).replace('','')
s_split = re.split('\.',sentences)
sentencecount = len(s_split)-1


# Finding the average letter count
letters = re.sub("[\., \-')()><\n]", '', lines).replace('','')
letteravg = round(len(letters)/len(wordsplit),2)

# Finding the average sentence length
avgsent = round(len(wordsplit)/len(s_split),2)

# Creating a list to print and write output of results
results = (

            f"Paragraph Analysis\n"
            f"---------------------\n"
            f"Approximate Word Count: {wordcount}\n"
            f"Approximate Sentence Count: {sentencecount}\n"
            f"Average Letter Count: {letteravg} \n"
            f"Average Sentence Length: {avgsent}  \n"

            )

# Print results
print(results)


# Providing outpath to where it will write the new paragraph1_resuls.txt
outpath = os.path.join('Resources','paragraph1_results.txt')


# Opening and writing results to new file
with open(outpath,'w')as textfile:
    textfile.write(results)
    
# Done with file, now closing it
f.close()


