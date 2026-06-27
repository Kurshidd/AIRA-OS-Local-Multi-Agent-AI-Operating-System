import logging


logging.basicConfig(

    filename="aira.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)


class AgentLogger:

    @staticmethod
    def info(message):

        logging.info(message)

    @staticmethod
    def error(message):

        logging.error(message)