import datetime
import winsound

def alarmBuzz(getTime):
    fTime = str(datetime.datetime.now().strptime(getTime,' %I:%M %p'))
    fTime = fTime[11:-3]
    hourReal = fTime[:2]
    hourReal = int(hourReal)
    minReal = fTime[3:]
    minReal = int(minReal)

    while(True):
        if hourReal == datetime.datetime.now().hour:
            if minReal == datetime.datetime.now().minute:
                print('.',end="")
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif minReal<datetime.datetime.now().minute:
                break
if __name__ == "main":
    print('This is the self-created module to set Alarm')