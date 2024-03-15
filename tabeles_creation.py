import mysql.connector
import sys
from dotenv import load_dotenv
import os

load_dotenv()
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("PASSWORD"),
        database="figures",
    )
    mycursor = mydb.cursor()
except Exception as e:
    print(e)
    sys.exit()


mycursor.execute(
    "CREATE TABLE results (SHAPE_ID int AUTO_INCREMENT, SHAPE varchar(100), AREA FLOAT(10,2), CIRCUIT FLOAT(10,2), PRIMARY KEY (SHAPE_ID));"
)

mycursor.execute(
    "CREATE TABLE parameters (SHAPE_ID int AUTO_INCREMENT, PARAMETERS varchar(100), PRIMARY KEY (SHAPE_ID));"
)

mycursor.execute(
    "ALTER TABLE parameters ADD CONSTRAINT SHAPE_ID FOREIGN KEY (SHAPE_ID) REFERENCES results(SHAPE_ID) ON DELETE CASCADE;"
)

mycursor.close()
mydb.close()
