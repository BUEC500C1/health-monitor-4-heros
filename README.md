# health-monitor-4-heros
health-monitor-4-heros created by GitHub Classroom.     
Our group has 4 members.    
Current integrated modules look like below:     
![draft](imgs/draftModule.PNG)   

## Alert Module section     
#### Description      
There are 4 main functions in alertMod function.   
#### Inputs for alertMod functions    
information from machine collected and value     
#### Outputs for alertMod functions     
Based on the value and threshold, our alert program will determine to alarm or send data to display.     
For sending data to display, it will call the url and post data:
```
# append data and record in log and send to users
url = 'https://127.0.0.1:5000/spo2'
s = json.dumps({ "value" : "100"})
# json.dumps({'key1': 'value1', 'key2': 'value2'})
r = requests.post(url, data=s)
# print(r.text)

print("sent data: " + mes + ".")
```
#### Details   
Please click [here](https://github.com/BUEC500C1/health-monitor-4-heros/tree/master/AlertModule) to see more details in images.    

## Display section    


## Data section     


## AI API section    


