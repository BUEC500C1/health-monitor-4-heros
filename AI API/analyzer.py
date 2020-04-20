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

if __name__ == '__main__':
    print(analyzer({'Pulse': 50, 'Blood_Pressure': 100, 'Oxygen_Level': 120}))
    print(analyzer({'Pulse': 120, 'Blood_Pressure': 60, 'Oxygen_Level': 90}))
    print(analyzer({'Pulse': 30, 'Blood_Pressure': 100, 'Oxygen_Level': 30}))
    print(analyzer({'Pulse': 50, 'Blood_Pressure': 10, 'Oxygen_Level': 100}))
    print(analyzer({'Pulse': 50, 'Blood_Pressure': 100, 'Oxygen_Level': 120}))
    print(analyzer({'Pulse': 120, 'Blood_Pressure': 60, 'Oxygen_Level': 30}))
    print(analyzer({'Pulse': 30, 'Blood_Pressure': 30, 'Oxygen_Level': 120}))
    print(analyzer({'Pulse': 100, 'Blood_Pressure': 70, 'Oxygen_Level': 100}))
    print(analyzer({'Pulse': 42, 'Blood_Pressure': 105, 'Oxygen_Level': 97}))

