import sqlite3 as sq
import pymysql
from config import host, user, password, db_name 

from datetime import datetime
now = datetime.now()
formatted_date = '"'+ now.strftime('%Y-%m-%d %H:%M:%S')+'"'


print(formatted_date)

#?----------------------------------INSERT T-----------------------------------------------------------------------------------------------------------------------
def insert_T(ind_id , indication , time , mean):

    connection = pymysql.connect(host = host,port = 3306,user = user,password = password,database = 'gholimp',cursorclass = pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `T_indication`(ind_id , indication, mean_values , time) VALUES ({ind_id} , {indication} , {mean} , {time});"
        cursor.execute(insert_query)
        connection.commit()

#?----------------------------------INSERT H----------------------------------------------------------------------------------------------------------------------
def insert_H(ind_id , indication , time , mean):
  
    connection = pymysql.connect(host = host,port = 3306,user = user,password = password,database = 'gholimp',cursorclass = pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `H_indication`(ind_id , indication, mean_values , time) VALUES ({ind_id} , {indication} , {mean} , {time});"
        cursor.execute(insert_query)
        connection.commit()
#?----------------------------------INSERT Hb--------------------------------------------------------------------------------------------------------------------
def insert_Hb(ind_id , indication , time , mean):
  
    connection = pymysql.connect(host = host,port = 3306,user = user,password = password,database = 'gholimp',cursorclass = pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        insert_query = f"INSERT INTO `Hb_indication`(ind_id , indication , mean_values , time) VALUES ({ind_id} , {indication} , {mean} , {time});"
        cursor.execute(insert_query)
        connection.commit()

#!----------------------------------DELETE T-----------------------------------------------------------------------------------------------------------------------
def delete_T():

    connection = pymysql.connect(host = host,port = 3306,user = user,password = password,database = 'gholimp',cursorclass = pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        delete_query = "DELETE FROM `t_indication` WHERE id < 1200 ;"  
        cursor.execute(delete_query)
        connection.commit()

#!----------------------------------DELETE H-----------------------------------------------------------------------------------------------------------------------
def delete_H():

    connection = pymysql.connect(host = host,port = 3306,user = user,password = password,database = 'gholimp',cursorclass = pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        delete_query = "DELETE FROM `h_indication` WHERE id < 1200 ;"  
        cursor.execute(delete_query)
        connection.commit()

#!----------------------------------DELETE HB-----------------------------------------------------------------------------------------------------------------------
def delete_HB():

    connection = pymysql.connect(host = host,port = 3306,user = user,password = password,database = 'gholimp',cursorclass = pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        delete_query = "DELETE FROM `hb_indication` WHERE id <  1200 ;"  
        cursor.execute(delete_query)
        connection.commit()

try:

    connection = pymysql.connect(
    host = host,
    port = 3306,
    user = user,
    password = password,
    database = 'gholimp',
    cursorclass = pymysql.cursors.DictCursor
    )
    print('Connected')

    try:

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `T_indication`(id int AUTO_INCREMENT ," \
        #                          "ind_id tinyint," \
        #                          "indication float ," \
        #                          "mean_values float ," \
        #                          "time datetime , PRIMARY KEY (id));" 
        #     cursor.execute(create_table_query)
        #     connection.commit()
        #     print('2 [!]TableCreated[!]')

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `H_indication`(id int AUTO_INCREMENT ," \
        #                          "ind_id tinyint," \
        #                          "indication float ," \
        #                          "mean_values float ," \
        #                          "time datetime , PRIMARY KEY (id));" 
        #     cursor.execute(create_table_query)
        #     connection.commit()
        #     print('2 [!]TableCreated[!]')

        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `Hb_indication`(id int AUTO_INCREMENT ," \
        #                          "ind_id tinyint," \
        #                          "indication float ," \
        #                          "mean_values float ," \
        #                          "time datetime , PRIMARY KEY (id));" 
        #     cursor.execute(create_table_query)
        #     connection.commit()            
        #     print('2 [!]TableCreated[!]')


        # with connection.cursor() as cursor:
        #     insert_query = f"INSERT INTO `THinfo`(ind_id , type , indication , time) VALUES (1 , 'air_temp' , 27.3 , '2021-07-17');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        # print('3 [!]DataInserted[!]')

        # with connection.cursor() as cursor:
        #     cursor.execute("SELECT * FROM `THinfo`")
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `THinfo` WHERE ind_id = 1 ;"  
        #     cursor.execute(delete_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `THinfo`;"  
        #     cursor.execute(drop_table_query)
        a = 2
    finally:
        connection.close()

except Exception as ex:
    print('Not Connected')   
    print(ex)

