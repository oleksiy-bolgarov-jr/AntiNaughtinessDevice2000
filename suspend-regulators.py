#!/usr/bin/python3

import datetime, psutil, os, signal, sys, time
from swap_characters import swap
from functions_and_constants import warn

print("""WARNING!
You are about to suspend the regulation script.
This script is there for your own good. It is suggested that you do not proceed.
Are you sure you want to do this? (Y/N)""")
answer = input()
if not answer.lower().startswith("y"):
    print("OK. Not suspending anything. Have a nice day.")
    sys.exit()
print("""
Please enter the number of minutes you would like to suspend the script and
press enter. If you wish for it to be suspended indefinitely, press enter 
without typing anything.
""")
answer = input()
minutes = None if not answer.isnumeric() else int(answer)
print("""
You will now be shown three statements one by one. For each statement, if you 
agree with it, then type it out exactly as it appears and press enter. If you
disagree with it, simply press enter without typing anything. Typing anything
other than the statement will also be counted as disagreement. Copying and
pasting the statement will not be accepted.

The first statement follows below:""")
statements = [
"I understand that the script I wish to suspend exists for my own good, and I am not allowed to suspend it except under extreme circumstances. By carrying out this command, I claim that there are extreme circumstances that require the suspension of the script.",
"I bear full responsibility for anything that happens as a result of carrying out this action, including lost productivity and health problems. Furthermore, if no extreme circumstances exist that warrant this action, then I am a disgusting liar and a fraud."
]
if minutes is None:
    statements.append("Since I have chosen to suspend the script indefinitely, it is my responsibility to make sure the suspension does not go on for longer than I need. Therefore, I will either shut down the computer or unsuspend the script as soon as the extreme circumstances are resolved. Furthermore, in the future, I will do my best to ensure that I do not need to do this again.")
else:
    statements.append("I am reasonably sure that the time I have chosen, {} minutes, is no more than I need for my situation. If it turns out to be more than necessary, I will shut down the computer or unsuspend the script when the situation has been resolved. Furthermore, in the future, I will do my best to ensure that I do not need to do this again.".format(minutes))

for statement in statements:
    print("\n" + swap(statement))
    if input() != statement:
        print("OK. Not suspending anything. Have a nice day.")
        sys.exit()

answer = input(
"\nThis is your last chance to disagree. Are you sure you wish to do this? (Y/N)"
)
if not answer.lower().startswith("y"):
    print("OK. Not suspending anything. Have a nice day.")
    sys.exit()

# The actual suspension
regulators_process = None
for p in psutil.process_iter():
    try:
        if p.name() == "regulators.py":
            regulators_process = p
            p.suspend()
    except psutil.NoSuchProcess:
        print("Sorry, process not found.")
        sys.exit(1)

pid = os.fork()
if pid == 0:
    if minutes is not None:
        print(("OK. The regulator script will be suspended for {} minutes, " + \
                "starting at {}.").format(minutes, time.asctime()))
        print("To unsuspend it early, use the following command: unsuspend-regulators.py")
        time.sleep(60*minutes)
        try:
            p.resume()
        except psutil.NoSuchProcess:
            warn("ERROR", 
                    "Something went wrong while trying to resume the regulation script. Please contact the developer.")
    else:
        print("OK. The regulator script will be suspended indefinitely.")
        print("To unsuspend it, use the following command: unsuspend-regulators.py")
        while True:
            time.sleep(1)
