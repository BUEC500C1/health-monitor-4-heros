# Display Module
A Restful Api Display module for a health monitor 
## 4 health status
There are 4 health status, SpO2, Blood Presser, HR, PR need to display. They have different entry points.
### SPO2 Entry point
```url
https://4heros.bu.edu/spo2
```
### BP Entry point
```url
https://4heros.bu.edu/bp
```
### HR Entry point
```url
https://4heros.bu.edu/hr
```
### PR Entry point
```url
https://4heros.bu.edu/pr
```
## Apis (use spo2 as a example)
### write data to screen
```url
[post] https://4heros.bu.edu/spo2/display
value = 100
```
If command runs sucessfully, module will return HTTP200.
### close screen
```url
[put] https://4heros.bu.edu/spo2/close
```
If command runs sucessfully, module will return HTTP200.
### get screen status
```url
[Get] https://4heros.bu.edu/spo2/status
```
#### return
```json
{
	"status": "running",
	"timeStamp": 1583189357
}
```
https://en.wikipedia.org/wiki/Unix_time
Click her for more information about the timeStamp
## Features
Data will expire in 2 seconds. For example if spo2's writing api doesn't be called over 2 second, the spo2 part of screen will display nothing.
