import os
import pyautogui as p
#import datetime
#import _datetime
from  datetime import datetime
import time

#d = datetime.datetime.now()
today = datetime.now()
d=today.strftime(r"%d.%m.%Y.%H.%M.%S")
dc=str(d)+'.jpg'
time.sleep(5)
p.screenshot().save(dc)
print("Screenshot saved")

