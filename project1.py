cosmetics = 0
perfumes = 0
medicine =0

import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeFormat = '{:02d}:{:02d}'.format(mins, secs)
        # print(timeformat,end="\r")
        time.sleep(1)
        time_sec -= 1
        print(timeFormat)


    print("try again later")