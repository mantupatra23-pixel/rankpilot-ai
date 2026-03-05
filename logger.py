import logging

logging.basicConfig(
    filename="rankpilot.log",
    level=logging.INFO
)

def log_event(message):

    logging.info(message)
