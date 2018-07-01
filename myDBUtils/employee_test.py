'''
Created on Jun 22, 2018

@author: karsu
'''

import os, sys
import pyodbc
import datetime
import logging
import db_utils as dbu

db_file = 'employee.accdb'  #raw string, escape sequences are ignored
db_file = os.path.abspath(db_file)    
conn = dbu.createDBConnection(db_file)
if conn == False:
    sys.exit()
    
table_name = "Employees"
field_names = ["LastName", "Job"]
 
#===============================================================================
# having_names = []
# operands = []
# values = []
#  
#===============================================================================

having_names = ["LastName","Job"]
operands = ["=", "="]
values = ["Sundar","Student"]
 
outrecs = dbu.get_unique_values(conn, table_name, field_names,having_names,operands,values)
#print(outrecs)

#===============================================================================
# employees_list = []
# table_name = 'Employees'
# 
# employees_list = dbu.get_all_recs(conn, table_name)
#===============================================================================


# for employee in employees_list:
#   for k, v in employee.items():
#        print(k, v)

#===DELETE all records=========================================================================
# dbu.delete_all_records(conn,table_name)
# print('All records from ' + table_name +' deleted')
#===============================================================================

#===DELETE Selective records===========================================================================
# field_names = ['FirstName', 'LastName']
# operands = ['=', '=']
# #    values = ['A','datetime.date(year=2018, month=3, day=15)']
# #values = ['A','#3/16/2018#']
# values = ["Krishna","Sundar"]
# 
# dbu.delete_selective_recs(conn,table_name,field_names,operands, values)
# print('delete completed')
#===============================================================================


#===============================================================================
# column_name = "Job"
# dbu.drop_a_column(conn, table_name, column_name)
#===============================================================================

#===============================================================================
# rec_count = dbu.get_record_count(conn,table_name)
# print(rec_count)
#===============================================================================

#===============================================================================
# sql = 'SELECT * FROM Employees'
# returned_data = dbu.execute_a_fetch_sql_stmt_directly(conn,sql)
# print(returned_data)
#===============================================================================

employee_out = {}
employee_out['FirstName'] = "Mita5"
employee_out['LastName'] = "Elan"
employee_out['Phone'] = "(908)111-1111"
employee_out['Email'] = "Mita@yahoo.com"
employee_out['Pay'] = "10000"
employee_out['Job'] = "Student"

#dbu.insert_recs(conn, table_name, employee_out)
#print('insert completed')
