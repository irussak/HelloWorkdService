import requests
import os

def send_request(url, method="GET", payload={}, headers={}):
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def count_characters(response):
    splited_response = list(response.replace(" ", ""))
    character_count = len(splited_response)
    return {"character_count": character_count}



def lambda_handler(event, context):
    url = os.environ.get("TARGET_URL")

    response = send_request(url=url)

    result = count_characters(response=response)

    return result