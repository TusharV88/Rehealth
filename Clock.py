# Clock
import time


def current_time():
    # Get the Current Time with pm or am and Day
    hr = str(time.strftime('%I'))
    min = str(time.strftime('%M'))
    sec = str(time.strftime('%S'))
    noon = str(time.strftime('%p'))
    day = str(time.strftime('%A'))
    year = str(time.strftime('%y'))
    date = str(time.strftime('%d'))
    month = str(time.strftime('%b'))


    return hr, min, sec, noon, day, year, date, month
