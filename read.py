from util import getconnection

def readtable (dbdetails,tablename,limit=0):
    sourcedb=dbdetails['SOURCE_DB']

    connection = getconnection(sourcedb['DB_TYPE'],sourcedb['DB_HOST'],sourcedb['DB_NAME'],sourcedb['DB_USER'],sourcedb['DB_PASS'])
    cursor=connection.cursor()
    if limit == 0:
        query = f"SELECT * FROM {tablename}"
        print(query)
    else:
        query = f'SELECT * FROM {tablename} LIMIT{limit}'

    cursor.execute(query)
    data = cursor.fetchall()
    columnname = cursor.column_names

    connection.close()

    return (data,columnname)

