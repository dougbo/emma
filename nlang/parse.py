#
# read in lines between paragraph mark (blank line)
# skip lines that are markup
# trim and join
# split into words and punctuation
# fix problems
# identify abbreviations
# identify conjunctions
# identify preps
# identify articles
# identify prep phrases
# identify suspect nouns
# identify suspect 
# identify suspect verbs
# identify suspect adverbs
# pull out quotations


import os
import re

DQUOTE = '"'
PERIOD = '.'

def process_para(lines):
    # collection of de-abbreviated lines
    # periods should represent sentence breaks
    sentences = [l.split() for l in ' '.join(lines)]
    sentences = sentences.replace('.', 'P.') \
        .replace('?', 'Q?') \
        .replace('!', 'E!')
    sentences = sentences.split('.?!')

    print('S: ', sentences)
    # return a list sentences, each sentence is a list of words in the sentence
    return sentences

blogfile = 'blogs/2059027.male.15.Student.Leo.xml'

with open(blogfile, "r") as fp:
    lines = []
    paras = []
    
    abbreviations = {
        r'(^|\w)dr.':'doctor',
        r'..[.][.]': 'ELIPSIS'
        }
    line = fp.readline()

    for line in fp.readlines():
        # process in lower case (replace some punctuation with upper case)
        line = line.strip().lower()

        if (len(line) == 0):
            # found a paragraph break
            print("zero")
            if (len(lines) > 0):
                paras += process_para(lines)
                lines = []
            continue

        if (line[0] == '<'): continue

        # replace abbreviations
        for abb, repl in zip(abbreviations, abbreviations.values()):
            line = re.sub(abb, repl, line)

        lines.append(line)


for para in paras:
    print("PAR: ", para)
