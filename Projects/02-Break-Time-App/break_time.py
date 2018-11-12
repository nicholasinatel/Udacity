# This Program
# STEP:0 - Count Time Upon Activation
# STEP:1 - If time = 2 hours : Take a Break
# STEP:2 - Open Browser With Video Song
# STEP:3 - Go back to Step:0

import webbrowser
import time

total_breaks = 2
break_count = 0
timer = 5

url = raw_input("Enter with desired URL: ")
# for var in (inicio, fim, passo)
for break_count in range( 0, total_breaks, 1):  
    time.sleep(timer) 
    # Suspends the program for given number of seconds  
    print(url)
    webbrowser.open(url)
