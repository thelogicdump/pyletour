import requests
from math import floor

def SecondsToMinutesSeconds(seconds):
    if seconds < 60:
        return "{0:n}".format(seconds)
    elif seconds < (60 * 60):
        minutes = floor(seconds/60)
        seconds = seconds - minutes * 60
        return "{0:n}:{1:02n}".format(minutes, seconds)
    else:
        hours = floor(seconds / (60 * 60))
        remainingSeconds = seconds - (hours * 60 * 60)
        minutes = floor(remainingSeconds / 60)
        seconds = remainingSeconds - (minutes * 60)
        return "{0:n}:{1:02n}:{2:02n}".format(hours, minutes, seconds)

