# This Program
# STEP:0 - Count Time Upon Activation
# STEP:1 - If time = 2 hours : Take a Break
# STEP:2 - Open Browser With Video Song
# STEP:3 - Go back to Step:0

import webbrowser
import time

total_breaks = 3
break_count = 1
for break_count in range( 1, total_breaks, 1):
    time.sleep(5)
    url = raw_input("Enter with desired URL: ")

    print(url)

    webbrowser.open(url)
