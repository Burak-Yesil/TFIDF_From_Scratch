import pandas as pd
docA = "good boy"
docB = "good girl"
docC = "boy girl good"

bowA = docA.split(" ")
bowB = docB.split(" ")
bowC = docC.split(" ")

wordSet = set(bowA).union(set(bowB)).union(set(bowC))
print(wordSet)

wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)
wordDictC = dict.fromkeys(wordSet, 0)

for word in bowA:
    wordDictA[word] += 1
for word in bowB:
    wordDictB[word] += 1
for word in bowC:
    wordDictC[word] += 1


def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict


tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)
tfBowC = computeTF(wordDictC, bowC)

print('TF --> sentence 1: ', tfBowA)
print('TF --> sentence 2: ', tfBowB)
print('TF --> sentence 3: ', tfBowC)


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        #         idfDict[word] = math.log10(N/float(val))
        idfDict[word] = math.log10((N+1)/(float(val)+1.0))+1
    return idfDict


idfs = computeIDF([wordDictA, wordDictB, wordDictC])


def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf


tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)
tfidfBowC = computeTFIDF(tfBowC, idfs)

pd.DataFrame([tfidfBowA, tfidfBowB, tfidfBowC])
