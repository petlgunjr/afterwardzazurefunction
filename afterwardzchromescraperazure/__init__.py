import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
  logging.info('Python HTTP trigger function processed a request.')
  try:
    logging.info(req)
    req_body = req.get_json()
    # infoProvided = json.loads(req_body)
    logging.info(req_body)
    return req_body["CurrentPrice"]
  except ValueError:
    return func.HttpResponse(
      "Could not parse json",
      status_code=400
    )
