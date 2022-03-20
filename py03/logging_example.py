import logging
 
logger = logging.getLogger()
console = logging.StreamHandler()

format_str = '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s'
console.setFormatter(logging.Formatter(format_str))

logger.addHandler(console) # prints to console.

logger.setLevel(logging.ERROR) 
try:
    logger.debug("Process is started")
    result = 5 / 0
except:
    logging.error("Error occured, details in below", exc_info = True)
    print("See after full error details")
