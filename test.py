import subprocess
import multiprocessing
import os
import signal
import sys
import time
proc1 = subprocess.Popen(args=['omxplayer','-o','both','val1.mp3'])
time.sleep(20)
subprocess.call(['pkill','-P',str(proc1.pid)])
proc1.kill()
