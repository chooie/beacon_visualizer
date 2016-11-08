import time, threading, functools

def clear_beacons():
    print 'Clearing beacons!'
    # Todo: Clear Beacons

def call_after_delay(func, time_delay_in_seconds):
    threading.Timer(time_delay_in_seconds, func).start()

def call_repeatedly(func, time_interval_in_seconds):
    call_after_delay(clear_beacons, time_interval_in_seconds)
    call_after_delay(functools.partial(call_repeatedly, func,
                                       time_interval_in_seconds),
                     time_interval_in_seconds)

def _run_on_start():
    call_repeatedly(clear_beacons, 1)
