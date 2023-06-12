import numpy as np
import pandas as pd
import statistics

def loadData(path):
    frame = pd.read_csv(path,header=None)
    return frame

def main():
    frame = loadData("1000_Random_Numbers.csv")
    print("mean: ")
    print(frame.mean())
    print("median: ")
    print(frame.median())
    print("mode: ")
    print(frame.mode())
    print("max: ")
    print(frame.max())
    print("min: ")
    print(frame.min())
    print("quantile([0.25, 0.5, 0.75])")
    print(frame.quantile([0.25, 0.5, 0.75]))
    return

main()