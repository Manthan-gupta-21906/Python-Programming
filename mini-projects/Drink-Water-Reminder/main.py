import time 
from plyer import notification
print("to terminate program click ctrl+c")
while True:
    print("please drink water")
    notification.notify(title="Please Drink Some Water", message="you need to drink some water",)

    time.sleep(60*60) #remind you in evey 1 hour 