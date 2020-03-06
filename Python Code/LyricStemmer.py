

from __future__ import print_function
from nltk.stem import *
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
import nltk
import os
import __future__
import re 
import numpy
import csv
import pandas as pd
import numpy as np
import math
import DbFunctions as db

def stemmWords(words):
    stemmer = PorterStemmer()
    for x in range(len(words)):
        stemmedWord = stemmer.stem(words[x])
        words[x] = stemmedWord
    return words



connection = db.GetCloudConnection()
songs = db.GetSongs(connection, "where ProcessedLyrics is not null")
processedLyrics = songs[['SongId','ProcessedLyrics']].to_numpy()
seperator = ' '

for x in range(len(processedLyrics)):
    words = []
    songId = processedLyrics[x][0]
    lyric = processedLyrics[x][1]
    for w in lyric.split():
        words.append(w)
    
    stemmedWords = stemmWords(words)
    newLyrics = seperator.join(stemmedWords)
    newconnection = db.GetCloudConnection()
    db.UpdateStemmedLyrics(newLyrics, songId, newconnection)







         