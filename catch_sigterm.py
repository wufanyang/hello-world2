import signal
import sys,time,datetime
 
def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)

while True:
    time.sleep(3)
    print datetime.datetime.now()
