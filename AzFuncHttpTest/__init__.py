import logging

import azure.functions as func


def main(req: func.HttpRequest, rating:func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_body()

    doc = func.Document.from_json(req_body)

    cosmosDbreqstatus = rating.set(doc)

    if cosmosDbreqstatus.status_code == 200:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully", 
            status_code=200)
    else : 
        return func.HttpResponse(
            "This HTTP triggered function executed successfully", 
            status_code = cosmosDbreqstatus.status_code)

    # if productID:
    #     return func.HttpResponse(f"The product name for your product id {productID} is Starfruit Explosion")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a productID in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
