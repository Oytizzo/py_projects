import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='test.log',
                    level=logging.DEBUG)

logging.debug("deBug log")
logging.info("inFo log")
logging.warning("warNing log")
logging.error("errOr log")
logging.critical("criTical log")
