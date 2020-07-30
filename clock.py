import time
import sys
import pyttsx3
from datetime import datetime
def do_callout(time_string):
    string = "It is "+time_string+"."
    print(string)
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()

callout_interval = 0
callout_happened = {}
current_time = 0
if __name__ == "__main__":
    callout_interval = int(sys.argv[1])
    while(True):
        current_time = int(time.time())%86400
        if(current_time == 0):
            callout_happened = {}
        time_string = str(current_time)
        if((current_time % (callout_interval*60)) == 0):
            if(not callout_happened.get(current_time)):
                callout_happened[current_time] = True
                do_callout(datetime.strftime(datetime.now(), "%I:%M %p"));
        time.sleep(0.5)

