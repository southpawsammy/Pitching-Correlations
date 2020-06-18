## finding a correlation between swing and miss rates of pitchers and the average break on their pitches
#Samuel Neal

import pandas as pd 


def printLines(count):
    bullpen = pd.read_csv('pitchingAVGBreaks.csv')
    #printing 15 rows for visualization 
    print(bullpen.head(count))