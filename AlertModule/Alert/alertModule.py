'''
4 main functions:    
Receive message   
Set threshold  
Alarm    
Send data to display    
'''

# import needed libraries    
import sys
import time
import requests
import json
import urllib3

# receive information    
def recMsg(msg, val):
  # Once we did not receive data, 
  # we will request again from traffic control for information.
  try:
    if msg is None: # The variable
      print('Message is None')
      # call a for loop to remind user
      for i in range(3):
        msg2 = input("please type in a value for msg")
        alertMod(msg2, val)
  except NameError:
    print ("This message is not defined")
  else:
    print ("Message is received and has a value")

# set threshold to compare with received value   
def setThre(val, msg1, msg2, msg3, msg4):
  # Once there is no threshold, set up a new one.
  th = 100 # test value for threshold, we can change based on collected information  
  usrVal = int(val)

  if usrVal > th:
    print("Current value is bigger than threshold, alarm and program ends!")
    alarm()
    time.sleep(1)
    sys.exit()
  elif usrVal == th:
    print("Current value is same to threshold, warning! Sending data to display...")
    time.sleep(2)
    sendData(msg1, msg2, msg3, msg4)
  else:
    print("Current value is less than threshold, ok! Sending data to display...")
    time.sleep(2)
    sendData(msg1, msg2, msg3, msg4)

# alarm function    
def alarm():
  # alarm user for several times    
  for i in range(3):
    print("Val is too big, alarm!")
    time.sleep(5)
    # after 5s sleep, we give another 3 times alarm
    print("Val is too big, alarm!")
    time.sleep(5)
    # after 5s sleep, we give another 3 times alarm - last time
    print("Val is too big, alarm!")


# send data as post method to display API
def sendData(msg1, msg2, msg3, msg4):
  # spo2 bp hr awrr --- "SpO2", "Blood Pressure", "HR", "PR"
  kindsInfo = ["spo2", "bp", "hr", "awrr"]
  dataInfo = [msg1, msg2, msg3, msg4]

  for i in range(4):
    url = 'http://127.0.0.1:5000/' + kindsInfo[i]
    info = dataInfo[i]
    s = json.dumps({ "value" : info })
    #print(info)
    #print(type(info))
    r = requests.post(url, data=s, verify=False)
    print(r.text)

  mes = msg1+'/'+ msg2 + '/'+ msg3 +'/' + msg4
  # after post data to url, print the result
  print("sent data: " + mes + ".")

# alert module    
def alertMod(msg, val):
  recMsg(msg, val)
  
    

if __name__ == '__main__':
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  msg1 = input("type in value for Sp02 \n")
  msg2 = input("type in value for Blood Pressure \n")
  msg3 = input("type in value for HR \n")
  msg4 = input("type in value for PR \n")
  # i.e. "{'Blood_Pressure': 100, 'Pulse': 75, 'Oxygen_Level': 340}"      
  msg = msg1+'/'+ msg2 + '/'+ msg3 +'/' + msg4

  val = input("type in an int value \n")
  # based on blodd pressure value, we set threshold to compare with, in this example is 100.   

  alertMod(msg, val)
  setThre(val, msg1, msg2, msg3, msg4)
