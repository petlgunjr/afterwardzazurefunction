import logging
import json
from geocodio import GeocodioClient
import azure.functions as func
import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=wardzwall.database.windows.net.aftwall;DATABASE=afterwardz;UID=apiTEST;PWD=Te$This1OuttatHere;")

cursor = conn.cursor()
results = cursor.execute("SELECT location FROM Geodata")
logging.info(results)
