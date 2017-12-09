import time
import sys
for i in range(100):
    sys.stdout.write("Download progress: %d%%   \r" % (i) )
    sys.stdout.flush()
    time.sleep(0.1)
