import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", filename="my_server_log.log",level=logging.DEBUG)

logging.getLogger()

logging.info("this is info")

logging.warning("this may break")

logging.error("this is error,fixed it")

logging.critical("this is crritical,fixed it")



