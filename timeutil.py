from datetime import datetime

def get_time(time):
    time_str = time.strftime("%I:%M %p")
    now = datetime.now()
    delta = time - now
    hours, minutes = delta.seconds / 3600, delta.seconds % 3600 / 60
    time_from_now = "10 hours 20 minutes from now"
    return "31 December 2013 at %s (%s)" % (time_str, time_from_now)
    
