# ngram.py
# Author: Joe Williams
import operator
import time

# 1. Get filedata from all files
# 2. Preprocess and split data accordingly
# 3. Write results to files

# Takes a file that has a list of files
def getInputFiles(filelist):
    stream = open(filelist)
    fileArray = stream.read().split("\n")
    stream.close()
    return fileArray

# Removes most special characters and caps
def preprocess(line):
    line = line.lower()
    for p in ['!','?',',','.',':',';','}','{','`','"','[',']','\n']:
        line = line.replace(p,'')
    return line

# get ngram from the data
def getNgrams(n,data):
    ngrams = {}
    text = preprocess(data.replace('\n',' '))
    nArr = ngram(n,text.split(' '))
    for l in nArr:
        if l == "": continue
        if not l in ngrams: ngrams[l] = 1
        else: ngrams[l] = ngrams[l] + 1
    return ngrams

# get ngram from the list
def ngram(n,l):
    nl = l[:n]
    grams = [' '.join(nl)]
    for i in l[n:]:
        if str(i) == '': continue
        nl.pop(0)   
        nl.append(i)
        grams.append(' '.join(nl))
    return grams

# returns a dictionary of the characters and their occurences
def getChars(data):
    charHash = {}
    charArr = list(preprocess(data.replace('\n',' ')))
    for c in charArr:
        if ord(c.lower()) < 97 or ord(c.lower()) > 122: continue
        if not c in charHash: charHash[c] = 1
        else: charHash[c] = charHash[c] + 1
    return charHash

# returns a 
def getFileData(files):
    data = ""
    for file in files:
        print("Reading %s..." % file.split('/')[-1])
        data += open(file).read()
    return data

# Execution..
filedata = getFileData(getInputFiles("input-files.txt"))

with open("characters.txt","w") as file:
    print("Writing Characters")
    for k, v in sorted(getChars(filedata).items(), key=operator.itemgetter(1)):
        file.write("%s:\t%d\n" % (k, v))

with open("unigrams.txt","w") as file:
    print("Writing Unigram")
    for k, v in sorted(getNgrams(1,filedata).items(), key=operator.itemgetter(1)):
        file.write("%s:\t%d\n" % (k, v))
    
with open("bigrams.txt","w") as file:
    print("Writing Bigrams")
    for k, v in sorted(getNgrams(2,filedata).items(), key=operator.itemgetter(1)):
        file.write("%s:\t%d\n" % (k, v))
    
with open("trigrams.txt","w") as file:
    print("Writing Trigrams")
    for k, v in sorted(getNgrams(3,filedata).items(), key=operator.itemgetter(1)):
        file.write("%s:\t%d\n" % (k, v))
print("Done ")