def patient_alarm(dictionary):
    result = []
    if dictionary['Pulse'] > 60 or dictionary['Pulse'] < 20:
        if dictionary['Pulse'] > 60:
            result.append('Note: High Pulse Alarm!')
        else:
            result.append('Note: Low Pulse Alarm!')
    if dictionary['Blood_Pressure'] > 140 or dictionary['Blood_Pressure'] < 80:
        if dictionary['Blood_Pressure'] > 140:
            result.append('Note: High Blood Pressure Alarm!')
        else:
            result.append('Note: Low Blood Pressure Alarm!')
    if dictionary['Oxygen_Level'] > 110 or dictionary['Oxygen_Level'] < 60:
        if dictionary['Oxygen_Level'] > 110:
            result.append('Note: High Blood Oxygen Alarm!')
        else:
            result.append('Note: Low Oxygen Level Alarm!')
    if not result:
        result.append('You look healthy!')
    return result

def main():
    print(patient_alarm({'Pulse': 50, 'Blood_Pressure': 100, 'Oxygen_Level': 120}))
    print(patient_alarm({'Pulse': 120, 'Blood_Pressure': 60, 'Oxygen_Level': 90}))
    print(patient_alarm({'Pulse': 30, 'Blood_Pressure': 100, 'Oxygen_Level': 30}))
    print(patient_alarm({'Pulse': 50, 'Blood_Pressure': 10, 'Oxygen_Level': 100}))
    print(patient_alarm({'Pulse': 50, 'Blood_Pressure': 100, 'Oxygen_Level': 120}))
    print(patient_alarm({'Pulse': 120, 'Blood_Pressure': 60, 'Oxygen_Level': 30}))
    print(patient_alarm({'Pulse': 30, 'Blood_Pressure': 30, 'Oxygen_Level': 120}))
    print(patient_alarm({'Pulse': 100, 'Blood_Pressure': 70, 'Oxygen_Level': 100}))

if __name__ == '__main__':
    main()
