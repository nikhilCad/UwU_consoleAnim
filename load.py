import time
import sys


animation = "UwU "

for i in range(100):
    time.sleep(0.05)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("End!")
