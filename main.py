from application.salary import calculate_salary
from application.db.people import people_wage, get_employees
import datetime
import pytest_parallel

if __name__ == '__main__':
    print(datetime.datetime.date(datetime.datetime.today()))
    get_employees(people_wage)
    calculate_salary(people_wage)