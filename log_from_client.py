from google.auth import jwt
import requests
import json
import base64

from requests.models import Response
from werkzeug.datastructures import IfRange

# Message data
json_payload = {
    "logName": "projects/cliu201/logs/clientlog",
    "entries": [
        {
            "jsonPayload": {
                "id": "1",
                "name": "1"
            }
        },
        {
            "jsonPayload": {
                "id": "2",
                "name": "2"
            }
        }
    ],
    "resource": {
        "type": "generic_node",
        "labels": {
            "game_name": "cliu201-game",
            "project_id": "cliu201"
        }
    }
}


# change the jwt_url as the new deploy'e cloud run's endpoint
jwt_url = 'https://gettoken-gygrgrxnnq-uc.a.run.app/api'
logging_url = "https://logging.googleapis.com/v2/entries:write"


def getToken():
    try:
        r = requests.get(jwt_url, timeout=30)
        # print(r.url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# Publish the message


def publish_with_jwt_request(access_token, url):
    # Request Headers
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'content-type': 'application/json'
    }

    # Get response data
    response = requests.post(url, headers=headers, json=json_payload)
    if response.status_code == 401:
        return 401

    print(response.status_code, response.content)


def main():
    response = getToken()
    access_token = json.loads(response)['access_token']
    # print(jwt_token)
    # print(a)

    publish_with_jwt_request(access_token, logging_url)
    print(json_payload)
        


if __name__ == '__main__':
    main()
