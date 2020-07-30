import time
import sys
import pyttsx3
def do_callout(minutes, remaining):
    string = ""
    if minutes == 1:
        string = "1 minute passed. "
    else: string = ("{} minutes passed. ".format(minutes))

    if remaining == 1:
        string += "1 minute remaining."
    elif remaining == 0:
        string+= "Time's up. Hand in the exam."
    else: string+= "{} minutes remaining.".format(remaining)
    print(string)
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()

startTime = 0
endTime = 0
secondsPassed = 0
callout_interval = 0
callout_happened = {}
if __name__ == "__main__":
    duration = int(sys.argv[1])* 60
    callout_interval = int(sys.argv[2])
    startTime = currentTime = int(time.time())
    endTime = startTime + duration
    while(startTime + secondsPassed <= endTime):
        secondsPassed = int(time.time())-startTime
        if((secondsPassed % (callout_interval*60)) == 0):
            if(not callout_happened.get(secondsPassed)):
                callout_happened[secondsPassed] = True
                minutes_passed = int(secondsPassed/60)
                minutes_remaining = int(duration/60)-minutes_passed
                do_callout(minutes_passed, minutes_remaining)
        time.sleep(0.5)


