from python.application.db.people import get_employees
from python.application.salary import calculate_salary
import datetime

if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%d.%M.%Y %I:%M"))
    calculate_salary()
    get_employees()