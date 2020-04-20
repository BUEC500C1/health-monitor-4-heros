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

def analyzer(dict):
    result = []
    if dict['Pulse'] > 60 or dict['Pulse'] < 20:
        if dict['Pulse'] > 60:
            result.append('Note: High Pulse Alarm!')
        else:
            result.append('Note: Low Pulse Alarm!')
    if dict['BloodPressure'] > 140 or dict['BloodPressure'] < 80:
        if dict['BloodPressure'] > 140:
            result.append('Note: High Blood Pressure Alarm!')
        else:
            result.append('Note: Low Blood Pressure Alarm!')
    if dict['BloodOxygen'] > 110 or dict['BloodOxygen'] < 60:
        if dict['BloodOxygen'] > 110:
            result.append('Note: High Blood Oxygen Alarm!')
        else:
            result.append('Note: Low Oxygen Level Alarm!')
    if not result:
        result.append('You look healthy!')
    return result

def main():
    dict1 = Predictor("data")
    dict2 = analyzer(dict1)
    print(dict2)
main()



