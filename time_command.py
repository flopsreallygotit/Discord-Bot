import datetime
import time

def now():
    time_now = datetime.datetime.now()
    return time_now

def time_now():
    now_time = datetime.datetime.now()
    t = now_time.strftime('%H:%M')
    return t
    
    
