# A simple loop that counts to 100 and resets

import time

x = 0
while x < 100:
    x += 1
    print("%d %d" % (x, x))
    if x == 100:
        print("Reached 100!")
        x = 0
    time.sleep(0.1)
