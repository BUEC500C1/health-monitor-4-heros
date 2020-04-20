import pandas as pd
import numpy as np

def Predict(Pulse,BloodPressure,OxygenLevel):
    return np.mean(Pulse), np.mean(BloodPressure),np.mean(OxygenLevel)

def Predictor(file):
    fileIn = pd.read_csv(file+'.csv')
    Pulse = fileIn.iloc[:,0].values
    BloodPressure = fileIn.iloc[:,1].values
    OxygenLevel = fileIn.iloc[:,2].values
    a,b,c = Predict(Pulse,BloodPressure,OxygenLevel)
    
    dict = {}
    dict["Pulse"] = int(a)
    dict["Blood_Pressure"] = int(b)
    dict["Oxygen_Level"] = int(c)
    return dict

print(Predictor("data"))

if __name__ == 'main':
    dict_precition = Predictor("data")