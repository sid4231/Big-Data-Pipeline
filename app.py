import sys
from config import DB_DETAILS
#from util import get_tables
#from read import readtable


def main():
    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)
    print(db_details)


if __name__ == '__main__':
    main()




