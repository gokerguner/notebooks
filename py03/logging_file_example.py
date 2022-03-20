import logging
 
logging.basicConfig(filename="logfile.txt", 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filemode='w',
                    level = logging.ERROR)
 
logger = logging.getLogger("example_logger")
 
try:
    logger.debug("Process is started")
    result = 5 / 0
except:
    logger.error("Exception thrown", exc_info = True)
    print("You will not see this line in the log file")