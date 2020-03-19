# Display Module
A Restful Api Display module for a health monitor 
## 4 health status
There are 4 health status, SpO2, Blood Presser, HR, PR need to display. They have different entry points.
### Entry point
```url
https://4heros.bu.edu/
```
## Apis
### write data to screen
```url
[post] https://4heros.bu.edu/spo2/display
{"name"="spo2","value" = 100}
```
If command runs sucessfully, module will return HTTP200.
### get screen status
```url
[Get] https://4heros.bu.edu/spo2
```
#### return
```json
{
	"name":"spo2"
	"status": "running",
	"timeStamp": 1583189357
}
```
https://en.wikipedia.org/wiki/Unix_time
Click her for more information about the timeStamp
## Features
Data will expire in 2 seconds. For example if spo2's writing api doesn't be called over 2 second, the spo2 part of screen will display nothing.
