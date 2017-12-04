import signal
import sys,time,datetime
import logging


log_path = '/var/log/catch_sigterm.log'
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler(log_path)
formatter = logging.Formatter(
    '%(pathname)s %(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    logger.info('got SIGTERM')
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)

while True:
    time.sleep(3)
    print datetime.datetime.now()
    logger.info(datetime.datetime.now())

