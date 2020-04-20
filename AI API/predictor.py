import pandas as pd
import numpy as np

def Predict(Pulse,BloodPressure,BloodOxygen):
    return np.mean(Pulse), np.mean(BloodPressure),np.mean(BloodOxygen)

def Predictor(file):
    fileIn = pd.read_csv(file+'.csv')
    Pulse = fileIn.iloc[:,0].values
    BloodPressure = fileIn.iloc[:,1].values
    BloodOxygen = fileIn.iloc[:,2].values
    a,b,c = Predict(Pulse,BloodPressure,BloodOxygen)
    
    dict = {}
    dict["Pulse"] = int(a)
    dict["BloodPressure"] = int(b)
    dict["BloodOxygen"] = int(c)
    return dict

print(Predictor("data"))

if __name__ == 'main':
    dict_precition = Predictor("data")