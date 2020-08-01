import pandas as pd
from config import DBDETAILS
from mysql import connector as mc
from mysql.connector import errorcode as ec


def loaddbdetails(env):
    return(DBDETAILS[env])


def mysqlconnection(dbhost,dbname,dbuser,dbpass):
    try:
        connection = mc.connect(user = dbuser,
                   password =dbpass,
                   host = dbhost,
                   database =dbname)
    except mc.errors as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("Invalid Credentials")
    return (connection)

def getconnection(dbtype,dbhost,dbname,dbuser,dbpass):
    connection = None
    if dbtype == 'mysql':
        connection = mysqlconnection(dbhost,dbname,dbuser,dbpass)
    return connection


def get_tables(path):
    tables = pd.read_csv(path, sep=":")
    return(tables.query('to_be_loaded=="yes"'))

