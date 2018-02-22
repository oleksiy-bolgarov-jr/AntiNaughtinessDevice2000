#!/usr/bin/python3

import psutil, sys
from functions_and_constants import warn

success_suspend = False
success_main = False

for p in psutil.process_iter():
    if p.name() == "suspend-regulators.py":
        try:
            p.terminate()
            success_suspend = True
        except psutil.NoSuchProcess:
            print("suspend.py not found. Skipping.")
    elif p.name() == "regulators.py":
        try:
            p.resume()
            success_main = True
        except psutil.NoSuchProcess:
            print("An error occurred while trying to resume regulators.py. Please report this to the developer.")

if success_suspend and success_main:
    print("SUCCESS: The regulator script has successfully been resumed.")
elif success_suspend and not success_main:
    print("ERROR: Failed to resume regulators.py. suspend.py successfully terminated. This is a bug. Please report this to the developer.")
    sys.exit(1)
elif not success_suspend and success_main:
    print("MOSTLY SUCCESS: The regulator script appears not to have been suspended in the first place.")
else: 
    print("ERROR: Terminating suspend.py and resuming regulators.py both failed. This is a bug. Please report this to the developer.")
    sys.exit(2)
