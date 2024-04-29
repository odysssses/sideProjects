#Just testing threading lmao
import threading 
from msvcrt import kbhit
from time import sleep

class Timer:
    def timer():
        hrs = 0
        mins = 0
        secs = 1
        while True:
            print(f"{hrs}:{mins}:{secs}", end="")
            if secs == 60:
                mins+=1
                secs = 0
            if mins == 60:
                hrs+=1
                mins = 0
            secs+=1
            if kbhit():
                break
            sleep(1)
            print("\r",end="")
        print(f"\r Timer stopped at: {hrs}:{mins}:{secs-3}")
        time = 5
        for i in range(1,6):
            print(f"\rExiting in: {time}", end="")
            sleep(1)
            time-=1
        exit()



print("Press any key to stop the timer")
timer1 = threading.Thread(target=Timer.timer, args=())
timer1.start()

