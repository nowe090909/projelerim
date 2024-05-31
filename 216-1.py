import sys
import time

def animate():
    for i in range(10):
        sys.stdout.write("\rLoading" + "." * i)
        sys.stdout.flush()
        time.sleep(0.5)

    sys.stdout.write("\n")

animate()