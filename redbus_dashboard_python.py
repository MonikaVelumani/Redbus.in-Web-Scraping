import mysql.connector
from datetime import datetime
from datetime import time
import pandas as pd
import streamlit as st
# MySQL connection details
host = 'localhost'
user = 'root'
password = '1234'
database = 'redbus'

# Connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
st.logo('https://s3.rdbuz.com/Images/rdc/rdc-redbus-logo.webp', link="https://www.redbus.in/", icon_image=None)
st.set_page_config(layout="wide")
st.header(':red[Redbus] Web Scraping', divider='rainbow')
st.title('A Project by Monica V :sunglasses:')

#State Filter
sql_query = "SELECT distinct (state) FROM bus_schedule;"

    # Execute the query
cursor.execute(sql_query)

    # Fetch all rows
rows = cursor.fetchall()
extracted_texts = [item[0] for item in rows]
option = st.sidebar.selectbox("State", extracted_texts)

#route filter
sql_query1 = "SELECT distinct (route) FROM bus_schedule where state = %s;"
cursor.execute(sql_query1, (option,))
rows = cursor.fetchall()
extracted_texts = [item[0] for item in rows]
optional = st.sidebar.selectbox("Route", extracted_texts)

# bus_type filter 
bus_tp = st.sidebar.selectbox("Bus Type", ("Any Type", "Seater", "Sleeper"))
if bus_tp == "Any Type":
    bus_tp = "%"
# AC bus_type filter 
bus_tp_ac = st.sidebar.selectbox("Bus Type", ("Any Type","A/C", "Non A/C"))
if bus_tp_ac == "Any Type":
    bus_tp_ac = "%"
# departure time 
dep_time = st.sidebar.selectbox("Departure Time", ("Any Time", "Before 6AM", "6AM to 12PM", "12PM to 6PM", "After 6PM"))
if dep_time =="Before 6AM":
    dep_st_tm = time(0,0,0)
    dep_end_tm = time(6,0,0)
elif dep_time =="6AM to 12PM":
    dep_st_tm = time(6,0,1)
    dep_end_tm = time(12,0,0)
elif dep_time =="12PM to 6PM":
    dep_st_tm = time(12,0,1)
    dep_end_tm = time(18,0,0)
elif dep_time =="After 6PM":
    dep_st_tm = time(18,0,1)
    dep_end_tm = time(23,59,59)
else:
    dep_st_tm = time(0,0,0)
    dep_end_tm = time(23,59,59)


ari_time = st.sidebar.selectbox("Arrival Time", ( "Any Time", "Before 6AM", "6AM to 12PM", "12PM to 6PM", "After 6PM"))
if ari_time =="Before 6AM":
    ari_st_tm = time(0,0,0)
    ari_end_tm = time(6,0,0)
elif ari_time =="6AM to 12PM":
    ari_st_tm = time(6,0,1)
    ari_end_tm = time(12,0,0)
elif ari_time =="12PM to 6PM":
    ari_st_tm = time(12,0,1)
    ari_end_tm = time(18,0,0)
elif ari_time =="After 6PM":
    ari_st_tm = time(18,0,1)
    ari_end_tm = time(23,59,59)
else:
    ari_st_tm = time(0,0,0)
    ari_end_tm = time(23,59,59)

#table
sql_query = f"""
    SELECT 
       state,
       route,
       bus_name,
       bus_type,
       CONCAT(    DATE_FORMAT(departure_time, '%H'), 'H:',    SUBSTR(DATE_FORMAT(departure_time, '%i'), 2), 'M' ) as Dep_time,
       duration,
       CONCAT(    DATE_FORMAT(arrival_time, '%H'), 'H:',    SUBSTR(DATE_FORMAT(arrival_time, '%i'), 2), 'M' ) as Ari_time,
       rating,
       price,
       seats_available
    FROM bus_schedule 
    WHERE state = '{option}' 
      AND route = '{optional}' 
      AND bus_type LIKE '%{bus_tp}%' 
      AND bus_type LIKE '%{bus_tp_ac}%' 
      AND departure_time > '{dep_st_tm.strftime('%H:%M:%S')}'
      AND departure_time < '{dep_end_tm.strftime('%H:%M:%S')}'
      AND arrival_time > '{ari_st_tm.strftime('%H:%M:%S')}'
      AND arrival_time < '{ari_end_tm.strftime('%H:%M:%S')}';
"""

df = pd.read_sql(sql_query, con=conn)

st.dataframe(df, width=1500, height=500 )


