import logging


def get_log():
    logging.basicConfig(level=logging.INFO, filename='logs/py_log.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')
