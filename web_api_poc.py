#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pyodbc
from flask import Flask
from flask import jsonify
app = Flask(__name__)
@app.route("/<table>/<country>/<startdate>/<enddate>")
def data(table, country, startdate, enddate):
    
    ##connection config
    server = 'testingdynamics.database.windows.net'
    database = 'TestDB'
    username = 'testing@testingdynamics'
    password = 'AIA-June2020!'   
    driver= '{ODBC Driver 13 for SQL Server}'

    ##connect to server, define query and extract data
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    sql = "Select * from dbo." + table + " where COUNTRY = '" + country + "' and INSERT_DATETIME between '" + startdate + "' and '" + enddate + "'"
    data = pd.read_sql(sql,cnxn)
    data = data.to_json(orient='records', date_format='iso')
    
    ##return data in json format
    return data

if __name__ == "__main__":
    app.run()


# In[1]:





# In[ ]:




