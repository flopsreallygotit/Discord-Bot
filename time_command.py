import datetime
import time

def now():
    time_now = datetime.datetime.now()
    return time_now

def timer(timer_time):
    if '.' in timer_time:
        timer=timer_time.split('.')
    if len(timer) == 3:
        timer_time=int(timer[0])*3600 + int(timer[1])*60 + int(timer[2])
    elif len(timer) == 2:
        timer_time=int(timer[0])*60 + int(timer[1])
    timer = time.sleep(int(timer_time))
    return timer

def time_now():
    now_time = datetime.datetime.now()
    t = now_time.strftime('%H:%M')
    return t
    
    
