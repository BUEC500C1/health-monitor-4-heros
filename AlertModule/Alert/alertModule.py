'''
4 main functions:    
Receive message   
Set threshold  
Alarm    
Send data to display    
'''

import sys
import time
import requests
import json

def recMsg(msg):
  # Once we did not receive data, 
  # we will request again from traffic control for information.
  try:
    if msg is None: # The variable
      print('Message is None')
      # call a for loop to remind user
      for i in range(3):
        msg2 = input("please type in a value for msg")
        alertMod(msg2)
  except NameError:
    print ("This message is not defined")
  else:
    print ("Message is received and has a value")


def setThre(val, msg):
  # Once there is no threshold, set up a new one.
  th = 10 # test value
  usrVal = int(val)

  if usrVal > th:
    print("Current value is bigger than threshold, alarm and program ends!")
    alarm()
    time.sleep(1)
    sys.exit()
  elif usrVal == th:
    print("Current value is same to threshold, warning! Sending data to display...")
    time.sleep(2)
    sendData(msg)
  else:
    print("Current value is less than threshold, ok! Sending data to display...")
    time.sleep(2)
    sendData(msg)


def alarm():
  # alarm user
  for i in range(3):
    print("Val is too big, alarm!")


def sendData(mes):
  # append data and record in log and send to users
  url = 'https://127.0.0.1:5000/spo2'
  s = json.dumps({ "value" : "100"})
  # json.dumps({'key1': 'value1', 'key2': 'value2'})
  r = requests.post(url, data=s)
  # print(r.text)

  print("sent data: " + mes + ".")


def alertMod(msg, val):
  recMsg(msg)
  setThre(val, msg)
    
if __name__ == '__main__':
  msg = input("type in sth for message \n")
  val = input("type in an int value \n")
  alertMod(msg, val);

