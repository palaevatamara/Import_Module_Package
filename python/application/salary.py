from colorama import Fore

from python.logger.logger import logger


@logger
def calculate_salary():
    print(Fore.RED + "Salary calculated")