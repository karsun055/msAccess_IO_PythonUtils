'''
Program Name: db_utils

Created on Jun 7, 2018

@author: karsu
'''

import pyodbc
import datetime
#import datetime
#import sys

def createDBConnection(db_file):
    user = 'admin'
    password = ''   
    odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)    #string variable formatted according to pyodbc specs
                
    try:
        conn = pyodbc.connect(odbc_conn_str)
    #            print("connection made")
    except Exception as e:
        print('Database connection is failed')
        print(e)
        return False               
    return conn

def getTableColumns(conn, table_name):
    c = conn.cursor()    
    sql = """ SELECT * FROM """
    sql = sql + table_name
    c.execute(sql)
    columns = [column[0] for column in c.description]
    return columns


def getTableColumnsDetails(conn, table_name):
    c = conn.cursor()    
    sql = """ SELECT * FROM """
    sql = sql + table_name
    c.execute(sql)
    return c.description


def getAllTablesInDB(conn):
    c = conn.cursor()
    tables = [table for table in c.tables() if table[3] == 'TABLE']    
    return tables

def getAllViewsInDB(conn):
    c = conn.cursor()
    views = [table for table in c.tables() if table[3] == 'VIEW']    
    return views

def get_all_recs(conn, tablename):
    
    c = conn.cursor()
    sql = """ SELECT * FROM """
    sql = sql + tablename
    c.execute(sql)

    columns = [column[0] for column in c.description]
    
    recs = []
    for row in c.fetchall():
        recs.append(dict(zip(columns, row)))
    
    return recs

def get_selective_recs(conn,table_name,field_names,operands, values):

    column_details = getTableColumnsDetails(conn, table_name)
    critera_list = list(zip(field_names, operands, values))
    
    c = conn.cursor()
    sql = " SELECT * FROM " + table_name + " WHERE "
    criteria_no = 0
    
    if (len(field_names) > 1):
        multiple_criteria = True
        
    for criteria in critera_list:
        criteria_no = criteria_no + 1
        
        sql = sql + "( [" + criteria[0] +"] " + criteria[1] + " "
        field_type = getFieldType(criteria[0], column_details)
        
        if (field_type ==  str):
            sql = sql + "'" + criteria[2] + "' )"

        if (field_type ==  datetime.datetime):
            sql = sql + criteria[2] + " )"
                                  
        if (multiple_criteria and criteria_no < len(field_names)):
            sql = sql + " AND "
        
    print(sql)
    c.execute(sql)

    columns = [column[0] for column in c.description]
    
    recs = []
    for row in c.fetchall():
        recs.append(dict(zip(columns, row)))
    
    return recs

def getFieldType(field_names,column_details):
    for rec in column_details:
        if (rec[0] == field_names):
            return rec[1]
        
def insert_recs(conn, table_name, outrec):
    
    columns = getTableColumns(conn, table_name)

    c = conn.cursor()
    
    sql = " INSERT INTO " + table_name + " (" + columns[0] + ", "
    
    for indx in range(1,len(columns)-1):
        sql = sql + columns[indx] +", "
    sql = sql + columns[-1] + ") values ( "
    for indx in range(1,len(columns)):
        sql = sql + " ?, "
        
    sql = sql +"?)"
#    print(sql)
    
    c.execute(sql, [v for k,v in outrec.items()])    
    conn.commit()

def delete_all_records(conn,table_name):
    
    c = conn.cursor()
    sql = "DELETE FROM " + table_name
    c.execute(sql)

def delete_selective_recs(conn,table_name,field_names,operands, values):

    column_details = getTableColumnsDetails(conn, table_name)
    critera_list = list(zip(field_names, operands, values))
    
    c = conn.cursor()
    sql = " DELETE * FROM " + table_name + " WHERE "
    criteria_no = 0
    
    if (len(field_names) > 1):
        multiple_criteria = True
        
    for criteria in critera_list:
        criteria_no = criteria_no + 1
        
        sql = sql + "( [" + criteria[0] +"] " + criteria[1] + " "
        field_type = getFieldType(criteria[0], column_details)
        
        if (field_type ==  str):
            sql = sql + "'" + criteria[2] + "' )"

        if (field_type ==  datetime.datetime):
            sql = sql + criteria[2] + " )"
                                  
        if (multiple_criteria and criteria_no < len(field_names)):
            sql = sql + " AND "
        
    print(sql)
    c.execute(sql)
    conn.commit()

def drop_a_column(conn, table_name, column_name):
    c = conn.cursor()
    sql = "ALTER TABLE " + table_name + " DROP COLUMN " + column_name
    print(sql)
#    ALTER TABLE [db].[username].[mytable] DROP COLUMN "TEMP CELCIUS
    c.execute(sql)
    conn.commit()
def get_record_count(conn,table_name):
    c = conn.cursor()
    sql = "SELECT COUNT (*) FROM " + table_name
    c.execute(sql)
    rowcount = c.fetchone()[0]
    return rowcount

def execute_a_fetch_sql_stmt_directly(conn,sql):
    c = conn.cursor()
    print(sql)
    c.execute(sql)
    recs = c.fetchall()
    return recs

def execute_a_non_fetch_sql_stmt_directly(conn,sql):
    c = conn.cursor()
#    print(sql)
    c.execute(sql)
    conn.commit()
    
#===============================================================================
# cursor.execute("SELECT COUNT (*) FROM fixtures")
# rowcount = cursor.fetchone()[0]
#===============================================================================

if __name__ == '__main__': 
    pass

    #==Insert code========================================================================
    # sql = """ insert into StooqCrossTabTable (Ticker, \
    # CurDate, \
    # PDayCloseTime, \
    # PDayOpen, \
    # PDayLow, \
    # PDayHigh, \
    # CDay0400PMVolume    
    # ) values \
    # (?,?,?,?,?,?,?) """
    #===========================================================================
    
    #==Insert Code========================================================================
    # c.execute(sql, \
    # outrec['Ticker'], \
    # outrec['CurDate'], \
    # outrec['PDayCloseTime'], \
    # outrec['PDayOpen'], \
    # outrec['PDayLow'], \
    # outrec['PDayHigh'], \
    # outrec['CDay0400PMVolume'])
    #===========================================================================