from database_package.people import get_employees
from accounting_package.salary import calculate_salary
from database_package.db_connection import *
from database_package.models import People, create_tables
from datetime import date
import emoji

create_tables(engine)

if __name__ == '__main__':
    current_date = date.today()
    print(current_date)
    get_employees()
    calculate_salary()
    print(emoji.emojize("I love Python :red_heart:"))

session.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
