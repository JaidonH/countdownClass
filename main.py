# Name: [Your Name]
# Date: 4/24/2022
# Project: Countdown Timer using Github
# File: countdownClass --> main.py
#-----------------------------------------------------------------
# Name: [Jaidon Hiestand]
# Date: 4/24/2022
# Project: Countdown Timer using Github
# File: countdownClass --> main.py
#-----------------------------------------------------------------
import time
def timerCountdown(userTime):

    while userTime:
        min,secs = divmod(userTime, 60)

        timer = '{:02d} : {:02d}'.format(min,secs)

        print('\r', timer, end='')

        time.sleep(1)

        userTime -= 1

    print('\n Timer Completed')

userTime = input('Please enter the time in seconds:\n')
print('Countdown until Melvin gets Pranked')
timerCountdown(int(userTime))
