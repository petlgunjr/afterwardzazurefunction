import logging
import json
from geocodio import GeocodioClient
import azure.functions as func
import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=wardzwall.database.windows.net.aftwall;DATABASE=afterwardz;UID=apiTEST;PWD=Te$This1OuttatHere;")

cursor = conn.cursor()
results = cursor.execute("SELECT location FROM Geodata")
logging.info(results)

client = GeocodioClient("fb531bb1bc80c53e5f0a88b5ff5efc30fbebc15")

def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  try:
    req_body = req.get_json()
    geocodioRequest = client.geocode(req_body["websiteAddress"], fields=["school"])
    # melissaRequest = await melissa.verify_address(req_body["websiteLocation"])
    geocodioResponse = json.dumps(geocodioRequest)
    # melissaResponse = json.dumps(melissaRequest)
    logging.info(geocodioResponse)
    return (geocodioResponse)
  except ValueError:
    return func.HttpResponse(
      "Could not parse json",
      status_code=400
  )
