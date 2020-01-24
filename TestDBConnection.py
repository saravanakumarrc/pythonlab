import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\MSSQLSERVER2017;'
                      'Database=AMSQASPRINT;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM UNITS')

for row in cursor:
    print(row)