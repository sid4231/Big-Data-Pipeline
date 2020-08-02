import sys
from config import DBDETAILS
from util import gettable
from read import readtable
import pandas as pd


def main():
    env = sys.argv[1]
    db_details = DBDETAILS[env]

    tablename = gettable('table_list')
    for t1 in tablename['table_name']:
        data,CN=readtable(db_details,t1)
        for data in data:
            print(data)





if __name__ == '__main__':
    main()




