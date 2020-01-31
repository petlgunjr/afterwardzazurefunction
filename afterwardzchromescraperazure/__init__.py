import logging
import json
from geocodio import GeocodioClient

import azure.functions as func

client = GeocodioClient("fb531bb1bc80c53e5f0a88b5ff5efc30fbebc15")

def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  try:
    req_body = req.get_json()
    location = client.geocode(req_body["Location"], fields=["school"])
    return json.dumps(location)
  except ValueError:
    return func.HttpResponse(
      "Could not parse json",
      status_code=400
    )
