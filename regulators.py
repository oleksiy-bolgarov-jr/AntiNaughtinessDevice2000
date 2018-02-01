#!/usr/bin/python3

# Oleksiy Bolgarov

# This script was made for my personal use so that I don't use the computer at
# night and end up sleeping and waking up late. It is intended to work in both
# Linux and Windows, but for now it only works on Linux. This is the version I 
# have decided to release to the public; therefore, all insults, swear words,
# and mentions of my name have been removed. If you wish to add insults and 
# swear words, please feel free to do so yourself.

# TODO: Add signal handler to prevent this process from being easily terminated
# TODO: Implement a way to temporarily suspend this script

import time, psutil
from time import sleep, localtime  # Python's time module

# Local imports
from classes import *
from functions_and_constants import *

class_schedule = [
        # No classes at this time.
        # If you want to add, for example, Monday from 14:00 to 16:00, add the
        # following item to this list:
        # Schedule(Time(14, 00), Time(2, 00), MONDAY)
       ]

psutil.Popen(["notify-send", "WELCOME", WELCOME_MESSAGE])

# First, check if this script was started during one of the forbidden times
curr_time_raw = time.localtime()
current_time = Time(curr_time_raw.tm_hour, curr_time_raw.tm_min)
current_weekday = curr_time_raw.tm_wday
no_internet_warned = False
# During class, or just before
for item in class_schedule:
    if item.weekday == current_weekday and \
        item.start_time <= current_time <= item.end_time:
        annoying_warn("ATTENTION", DURING_CLASS_MESSAGE)
        time.sleep(5*60) # 5 minutes
        shut_down()
    elif item.weekday == current_weekday and \
        item.start_time - TEN_MINUTES <= current_time <= item.end_time:
        annoying_warn("ATTENTION", BEFORE_CLASS_MESSAGE)
        time.sleep(10*60) # 10 minutes
        shut_down()
# At night
if SHUTDOWN_START_TIME <= current_time <= SHUTDOWN_END_TIME:
    annoying_warn("ATTENTION", NIGHT_MESSAGE)
    time.sleep(5*60) # 5 minutes
    shut_down()
elif SHUTDOWN_START_TIME - TEN_MINUTES <= current_time <= SHUTDOWN_END_TIME:
    annoying_warn("ATTENTION", BEFORE_NIGHT_MESSAGE)
    time.sleep(10*60) # 10 minutes
    shut_down()
# During "No Internet" time
elif NO_INTERNET_START_TIME <= current_time <= NO_INTERNET_END_TIME:
    warn("ATTENTION", NO_INTERNET_MESSAGE)
    no_internet_warned = True
elif NO_INTERNET_START_TIME - TEN_MINUTES <= current_time <= \
    NO_INTERNET_END_TIME:
    warn("ATTENTION", BEFORE_NO_INTERNET_MESSAGE_2)
    no_internet_warned = True

# Now start the loop
warned = False
while True:
    if not suspended():
        curr_time_raw = time.localtime()
        current_time = Time(curr_time_raw.tm_hour, curr_time_raw.tm_min)
        current_weekday = curr_time_raw.tm_wday

        # First, check school schedule
        for item in class_schedule:
            if not warned and item.weekday == current_weekday and \
                item.start_time - TEN_MINUTES <= current_time <= item.end_time:
                # Warn during the last 10 minutes before scheduled shutdown
                annoying_warn("ATTENTION", BEFORE_CLASS_MESSAGE)
                warned = True
            if item.weekday == current_weekday and \
                item.start_time <= current_time <= item.end_time:
                shut_down()

        # Next, check if it is night
        if not warned and \
            SHUTDOWN_START_TIME - TEN_MINUTES <= current_time <= \
            SHUTDOWN_END_TIME:
            # Warn during the last 10 minutes before scheduled shutdown
            annoying_warn("ATTENTION", BEFORE_NIGHT_MESSAGE)
            warned = True
        if SHUTDOWN_START_TIME <= current_time <= SHUTDOWN_END_TIME:
            shut_down()

        # Finally, check if "No Internet" time
        if not no_internet_warned and \
            NO_INTERNET_START_TIME - TEN_MINUTES <= current_time <= \
            NO_INTERNET_END_TIME and browsers_running():
            warn("ATTENTION", BEFORE_NO_INTERNET_MESSAGE_1)
            no_internet_warned = True
        if NO_INTERNET_START_TIME <= current_time <= NO_INTERNET_END_TIME:
            if not no_internet_warned:
                warn("ATTENTION", NO_INTERNET_MESSAGE_2)
                no_internet_warned = True
            kill_browsers()

    time.sleep(60)
