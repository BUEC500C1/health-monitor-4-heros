# Display Module
A Restful Api Display module for a health monitor 
## 4 health status
There are 4 health status, SpO2, Blood Presser, HR, PR need to display. They have different entry points.
### SpO2 Entry point
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
https://4heros.bu.edu/awrr	
```
## Apis (use spo2 as a example)
## Apis
### write data to screen
```url
[post] https://4heros.bu.edu/spo2
{"value" = "100"}
```
If command runs sucessful, module will return
```json
{
	"ok":"ok"
}
```

If command runs unsucessful, module will return
```json
{
	"error":"error"
}
```
### get screen status
```url
[Get] https://4heros.bu.edu/spo2
```
#### return
```json
{
	"name":"spo2",
	"status": "running",
	"timeStamp": 1583189357
}
```
https://en.wikipedia.org/wiki/Unix_time
Click her for more information about the timeStamp
