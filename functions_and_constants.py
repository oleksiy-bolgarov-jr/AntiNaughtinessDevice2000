import os, psutil, subprocess, sys, time

# Local imports
from classes import *

MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)

NO_INTERNET_START_TIME = Time(0, 30)    # 0:30 (12:30 AM)
NO_INTERNET_END_TIME = Time(8, 0)       # 8:00 (8:00 AM)
NO_INTERNET_DURATION = NO_INTERNET_END_TIME - NO_INTERNET_START_TIME

SHUTDOWN_START_TIME = Time(1, 45)       # 1:45 (1:45 AM)
SHUTDOWN_END_TIME = NO_INTERNET_END_TIME

FIVE_MINUTES, TEN_MINUTES = Time(0, 5), Time(0, 10)

# Add whatever browsers you have installed in the tuple below. The name must be
# the name of the process, since this code matches PIDs with names.
WEB_BROWSERS = ("firefox", "chromium-browse") 

WELCOME_MESSAGE = "This is a reminder that you are not allowed to use the Internet between the hours of 0:30 and 8:00. Any web browser you attempt to open during this period will instantly be terminated. Furthermore, you are not allowed to use the computer at all between the hours of 1:45 and 8:00, during class time, or in the hour before a class. Your computer will automatically shut down at these times."
BEFORE_NO_INTERNET_MESSAGE_1 = "It is now time to get off the Internet. Please close all Internet browser windows that are currently open, and do not open any new browser windows. You have 10 minutes to do this. If you fail to do this within this time, all open browsers will be forcefully terminated and you may lose data. Once all browser windows are closed, please shut down your computer and go to sleep. Good night."
BEFORE_NO_INTERNET_MESSAGE_2 = "This is a reminder that, in less than 10 minutes, you will not be allowed to use the Internet. If you attempt to open any web browser after the restricted time, the browser will be forcefully terminated. Please shut down your computer and go to sleep. Good night."
NO_INTERNET_MESSAGE = "This is a reminder that you are currently not allowed to use the Internet. If you attempt to open any web browser at this time, the browser will be forcefully terminated. Please shut down your computer and go to sleep. Good night."
NO_INTERNET_MESSAGE_2 = "Starting from this moment, you are no longer allowed to use the Internet for the rest of the night. If you attempt to open any web browser at this time, the browser will be forcefully terminated. Please shut down your computer and go to sleep. Good night."
BEFORE_CLASS_MESSAGE = "It is now time for you to get ready to go to class. Please save all your work, close all running applications, shower, get dressed, and go to class at this time. Your computer will shut down in 10 minutes."
DURING_CLASS_MESSAGE = "What the hell are you doing? Please get dressed and go to school immediately. Your computer will shut down in 5 minutes."
BEFORE_NIGHT_MESSAGE = "It is now time to get off your computer. Please save all your work, close all running applications, and go to bed. Good night. Your computer will shut down in 10 minutes."
NIGHT_MESSAGE = "You are not allowed to use your computer this late. Please go to bed immediately. Good night. Your computer will shut down in 5 minutes."
KILL_HEADING = "YOU HAVE COMMITTED A SERIOUS VIOLATION"
KILL_MESSAGE = "I'm sorry. I'm afraid I can't let you do that."


def warn(heading, message):
    raise Exception("Please use local files")
    if sys.platform == "linux" or sys.platform == "linux2":
        subprocess.Popen(
                ["/home/alexjr/Documents/Development/Bash/attention3times.sh",
                    message])  # TODO Add local link
        subprocess.Popen(["notify-send", "-u", "critical", heading, message])
    # TODO: Implement Windows (and possibly OS X) functionality

def annoying_warn(heading, message):
    raise Exception("Please use local files")
    if sys.platform == "linux" or sys.platform == "linux2":
        subprocess.Popen(
                ["/home/alexjr/Documents/Development/Bash/annoyingattention.sh",
                    message])  # TODO Add local link
        subprocess.Popen(["notify-send", "-u", "critical", heading, message])
    # TODO: Implement Windows (and possibly OS X) functionality

def browsers_running():
    for p in psutil.process_iter():
        try:
            if p.name() in WEB_BROWSERS:
                return True
        except psutil.NoSuchProcess:
            pass # Nothing needed here
    return False

def kill_browsers():
    for p in psutil.process_iter():
        try:
            if p.name() in WEB_BROWSERS:
                subprocess.Popen(["notify-send", "-u", "critical", KILL_HEADING,
                    KILL_MESSAGE])
                p.terminate()
        except psutil.NoSuchProcess:
            pass

def shut_down():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("shutdown -P now")
    else: # TODO: Include other OS, this is Windows
        os.system("shutdown /s /t 0")
    while True: time.sleep(1) # just in case

def suspended():
    """Return True iff this script has been suspended"""
    return False  # TODO: Implement a way to temporarily suspend this script
