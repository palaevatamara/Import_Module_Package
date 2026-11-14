from colorama import Back

from python.logger.logger import logger_param


@logger_param('get_employees.log')
def get_employees():
    print(Back.GREEN + "get_employees")