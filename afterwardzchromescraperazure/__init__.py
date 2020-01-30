import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  try:
    req_body = req.get_json()
    return json.dumps(req_body)
  except ValueError:
    return func.HttpResponse(
      "Could not parse json",
      status_code=400
    )
