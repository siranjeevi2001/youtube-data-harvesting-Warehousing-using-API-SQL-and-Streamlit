
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import pandas as pd


# Database connection string
DATABASE_URL = 'mysql+mysqlconnector://root:1022@localhost/youtube'

# Create database engine
engine = create_engine(DATABASE_URL)

def channel_list():
    try:
        # Query to select all records from the v_data table
        query = "select Channel_Name from channel_data;"
        
        tables_df = pd.read_sql(query, engine)
               
        # Return the DataFrame
        return tables_df
    except Exception as e:
        print("Error executing query:", e)



# Connect to MySQL server
def Mysql_engine():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database='youtube'
    )
    
    return conn
# def channel_table():
#     conn = Mysql_engine() 
#     if conn.is_connected():
#         # Query to select all tables in the database
#         query = "select * from channel_data;"
#         # Use pandas to read the query result into a DataFrame
#         tables_df = pd.read_sql(query, conn)
        
#         # Close the connection
#         conn.close()
#         # Print the DataFrame containing table names
#     return tables_df

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def channel_table():
    try:
        # Query to select all records from the v_data table
        query = "select * from channel_data;"
        
        tables_df = pd.read_sql(query, engine)
               
        # Return the DataFrame
        return tables_df
    except Exception as e:
        print("Error executing query:", e)


def playlist_table():
    try:
        # Query to select all records from the v_data table
        query = "select * from playlist_data;"
        
        tables_df = pd.read_sql(query, engine)
               
        # Return the DataFrame
        return tables_df
    except Exception as e:
        print("Error executing query:", e)

def vedio_table():
    try:
        # Query to select all records from the v_data table
        query = "select * from v_data;"
        
        tables_df = pd.read_sql(query, engine)
               
        # Return the DataFrame
        return tables_df
    except Exception as e:
        print("Error executing query:", e)


def comment_table():
    try:
        # Query to select all records from the v_data table
        query = "select * from comment_data;"
        
        tables_df = pd.read_sql(query, engine)
               
        # Return the DataFrame
        return tables_df
    except Exception as e:
        print("Error executing query:", e)


# ==========================================================================================================#
# count channel data
def channel_count():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = "SELECT COUNT(*) FROM channel_data;"
            mycursor.execute(query)
            result = mycursor.fetchone()[0]
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()


#playlist count 

# count playlist data
def playlist_count():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = "SELECT COUNT(*) FROM playlist_data;"
            mycursor.execute(query)
            result = mycursor.fetchone()[0]
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()



# count playlist data
def vedio_count():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = "SELECT COUNT(*) FROM v_data;"
            mycursor.execute(query)
            result = mycursor.fetchone()[0]
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()


# import mysql.connector

# def comment_count():
#     # Connect to MySQL database
#     mydb = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='1022',
#         database="youtube"
#     )

#     # Check if the connection is successful
#     if mydb.is_connected():
#         # Create a cursor object
#         mycursor = mydb.cursor()

#         try:
#             # Query to count all records in the comment_data table
#             query = "SELECT COUNT(*) FROM comment_data;"
#             mycursor.execute(query)
#             result = mycursor.fetchone()[0]
#             return (result)
#         except Exception as e:
#             print("Error executing query:", e)
#         finally:
#             mycursor.close()
#             mydb.close()

# # Create a cursor object
#         mycursor = mydb.cursor()

#         try:
#             # Query to count all records in the comment_data table
#             query = "SELECT COUNT(*) FROM comment_data;"
#             mycursor.execute(query)
#             result = mycursor.fetchone()[0]
#             return (result)
#         except Exception as e:
#             print("Error executing query:", e)
#         finally:
#             mycursor.close()
#             mydb.close()


# count comment data
def comment_count():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = "SELECT COUNT(*) FROM comment_data;"
            mycursor.execute(query)
            result = mycursor.fetchone()[0]
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()


# find recent increase data into database

def inc():
    # while True:
        temp = [0, 0, 0, 0]  # Initial values for comparison
        ch_count = channel_count()
        ch_result = ch_count - temp[0]
        temp[0] = ch_count  # Update the value in temp list
        
        pc = playlist_count()
        pc_result = pc - temp[1]
        temp[1] = pc  # Update the value in temp list
        
        vc = vedio_count()
        vc_result = vc - temp[2]
        temp[2] = vc
        
        cc = comment_count()
        cc_result = cc - temp[3]
        temp[3] = cc  # Update the value in temp list

        return ch_result, pc_result,vc_result, cc_result


# ------------------------------------------select query function --------------------------------------------

import streamlit as st
import pandas as pd
import mysql.connector

def Mysql_engine():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1022',
        database='youtube'
    )
    
    return conn

def query1():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """select  channel_data.Channel_Name,v_data.video_name from v_data 
                join channel_data on channel_data.Channel_Id = v_data.channel_id;"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()
def query2():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """SELECT v_data.channel_id, channel_data.Channel_Name, COUNT(video_id) AS video_count
                        FROM v_data 
                        join channel_data on channel_data.Channel_Id = v_data.channel_id
                        GROUP BY channel_id order by vedio_count desc limit 1;"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()

            
def query3():
    conn = Mysql_engine() 
    if conn.is_connected():
        mycursor = conn.cursor()
        try:
            query = """select v_data.view_count, v_data.video_name, channel_data.Channel_Name 
                       from v_data
                       join channel_data on channel_data.Channel_Id = v_data.channel_id
                       order by view_count desc
                       limit 10;"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return result
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()
def query4():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """select count(comment_id) as cc ,vedio_id, v_data.video_name from comment_data
                join v_data on v_data.video_id = comment_data.vedio_id
                group by vedio_id order by cc desc"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()
            
def query5():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """select (like_count) AS Highest_Like,video_name, channel_data.channel_name
            FROM v_data join channel_data on channel_data.channel_id = v_data.channel_id 
            order by Highest_Like desc limit 3;"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()
            
def query6():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """select like_count,video_name from v_data order by like_count desc;"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()
            

def query7():
    conn = Mysql_engine() 
    if conn.is_connected():
        mycursor = conn.cursor()
        try:
            query = """select Channel_Name, Channel_Views from channel_data order by Channel_Views desc"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return result
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()

def query8():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """SELECT published,video_name,channel_data.channel_name
                    FROM v_data join channel_data on channel_data.channel_id = v_data.channel_id
                    WHERE published LIKE '2022%'
                    order by published"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()
def query10():
    conn = Mysql_engine() 
    if conn.is_connected():
    # Create a cursor object
        mycursor = conn.cursor()
        try:
            # Query to count all records in the comment_data table
            query = """select vedio_id, count(comment_id) as cc , channel_data.channel_name from comment_data 
                    join v_data on v_data.video_id = comment_data.vedio_id
                    join channel_data on channel_data.channel_id = v_data.channel_id
                    group by(vedio_id) order by cc desc"""
            mycursor.execute(query)
            result = mycursor.fetchall()
            return (result)
        except Exception as e:
            print("Error executing query:", e)
        finally:
            mycursor.close()
            conn.close()