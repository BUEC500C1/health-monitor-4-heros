import pandas as pd
import numpy as np

def Predictor(file):
    fileIn = pd.read_csv(file + '.csv')
    Pulse = fileIn.iloc[:, 0].values
    BloodPressure = fileIn.iloc[:, 1].values
    BloodOxygen = fileIn.iloc[:, 2].values
    
    dic = dict()
    dic['Pulse'] = int(np.mean(Pulse))
    dic['BloodPressure'] = int(np.mean(BloodPressure))
    dic['BloodOxygen'] = int(np.mean(BloodOxygen))
    return dic

def main():
    dict1 = Predictor("data")
    print(dict1)
main()
