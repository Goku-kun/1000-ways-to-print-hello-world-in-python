from datetime import datetime as time, timedelta as at

# This will take a while...

clock = 0
noon = 12
schedule = [
    at(minutes = 1, seconds = 12),
    at(minutes = 1, seconds = 41),
    at(minutes = 1, seconds = 48),
    at(minutes = 1, seconds = 48),
    at(minutes = 1, seconds = 51),
    at(minutes = 0, seconds = 44),
    at(minutes = 0, seconds = 32),
    at(minutes = 1, seconds = 27),
    at(minutes = 1, seconds = 51),
    at(minutes = 1, seconds = 54),
    at(minutes = 1, seconds = 48),
    at(minutes = 1, seconds = 40),
    at(minutes = 0, seconds = 33)
    ]
stopwatch = 0
start = time.now()

while clock <= noon:
    stop = time.now()
    period = stop - start
    if period.total_seconds() > 1:
        start = time.now()
        stopwatch += 1
    if stopwatch == schedule[clock].total_seconds():
        print(chr(stopwatch), end = "")
        clock += 1
        stopwatch = 0
