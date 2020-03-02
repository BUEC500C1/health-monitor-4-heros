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
### close screen
```url
[put] https://4heros.bu.edu/spo2/close
```
### get screen status
```url
[Get] https://4heros.bu.edu/spo2/status
```
