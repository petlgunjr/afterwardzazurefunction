import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  try:
    return req.get_json()
  except ValueError:
    return func.HttpResponse(
      "Could not parse json",
      status_code=400
    )
