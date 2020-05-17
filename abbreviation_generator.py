#!/usr/bin/env python3

import re

#check camel case 2 words
def isCamelCase(word):
    #check for whitespaces
    res = bool(re.search(r"\s", word)) 
    if (not res):
        x = re.search(r"^[a-z](.+?)([A-Z])",word)
        if (x):
            return True
    return False


def camelCaseSplit(word):
    if (isCamelCase(word)):
        return re.split(r"(?=[A-Z])", word)
    else:
        return []
        


#core function
def createAbbr(word):
    if ( not word == ""  and (not word.isupper()) and isCamelCase(word)):
        if (isCamelCase(word)):
            SplitWords = camelCaseSplit(word)

        tempAcronym = ""
        if (len(SplitWords)!=0):
            for w in SplitWords:
                tempAcronym += w[0]
            return tempAcronym.upper()
        else:
            return ""
    else:
        return ""
    
def displayDict():
    print(abbrDict)

if (__name__=="__main__"):
    file_in_path = "words.txt"
    #dictionary for words
    abbrDict = {}

    with open(file_in_path) as f:
        fileWords = f.readlines()

    for word in fileWords:
        word = word.strip('\n').strip()
        abbreviation = createAbbr(word)

        if (abbreviation!="" and (len(abbreviation) > 1)):
            if (abbreviation in abbrDict):
                abbrDict[abbreviation].append(word)
            else:
                abbrDict[abbreviation] = [word]
    
if (__name__=="__main__"):
    displayDict()