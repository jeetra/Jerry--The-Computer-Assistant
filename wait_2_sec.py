import sys
from time import time

class Timer:
    def __init__(self,timer_period):
        """Initialise the timer
        >>> t = Timer(2)"""
        self.timer_period = timer_period
        self.update_timer()
    def update_timer(self):
        """Resets the timer to expire after <timer_period> seconds."""
        self.last_time = time()
        self.timer_expires = self.last_time + self.timer_period
    def has_timer_expired(self):
        """Call this function to check if the time has elapsed
        It will return 1 when time is up and reset the timer."""
        if time() > self.timer_expires:
            self.update_timer()
            return 1
        else:
            return 0

if __name__ == '__main__':
    # Setup a timer with a 2 second period
    t = Timer(2)

    while True:
        if t.has_timer_expired():
            #If the timer has expired, print Hello World.
            #print("Hello World")
            #sys.exit()
            break
