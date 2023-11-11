import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

def loadData(path):
    frame = pd.read_csv(path,header=None)
    return frame

def main():
    frame = loadData("1000_Random_Numbers.csv")
    print("mean: " + str(frame[0].mean()))
    print("median: " + str(frame[0].median()))
    print("mode: " + str(frame[0].mode())) # why does just the mode look different (format)
    print("max: " + str(frame[0].max()))
    print("min: " + str(frame[0].min()))
    print("quantile([0.25, 0.5, 0.75]): ")
    print(frame[0].quantile([0.25, 0.5, 0.75]))

    frame[0].hist(bins=50)
    plt.show()
    return

main()