from datetime import datetime

#def get_time(time, now=None):
def get_time(time, now=None):
    time_str = time.strftime("%I:%M %p")
    now = now or datetime.now()
    delta = time - now
    hours, minutes = delta.seconds / 3600, delta.seconds % 3600 / 60
    time_from_now = "%s hours %s minutes from now" % (hours, minutes)
    date_str = time.strftime("%d %B %Y (%Z)")
    return "%s at %s (%s)" % (date_str, time_str, time_from_now)
    
