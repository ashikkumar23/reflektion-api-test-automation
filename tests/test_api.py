"""
Title: API Tests
Author: Ashik Kumar
Date: 5 July 2019
"""

import json
import logging
from jsonschema import validate

from api import api

# Defining the schema in-order to match the json output
schema = {
        "type": ["array", "object"],
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
}

# URL
valid_test_url = "https://jsonplaceholder.typicode.com/posts"
invalid_test_url = "https://jsonplaceholder.typicode.com/invalidposts"

# Headers
headers = {"content-type": "application/json", "charset": "UTF-8"}

# Data which needs to sent as part of POST request
post_body = {"title": "foo", "body": "bar", "userId": 1}

# Data which needs to be sent as part of PUT request
put_body = {"id": 1, "title": "abc", "body": "xyz", "userId": 1}


def test_get_request_1():
    """
    Test to verify status code returned is 200 by GET request
    Test to verify the schema
    Test to verify GET request returns at-least 100 records
    :return: none
    """
    response = api.get_request(valid_test_url, headers)
    records = response.json()
    assert response.status_code == 200, "TEST FAIL - Status code is NOT 200, got: {}".format(response.status_code)
    validate(instance=records, schema=schema)  # Verify schema
    print(records)  # Print for debug
    assert len(records) >= 100, "TEST FAIL - GET request did NOT return 100 records, got: {}".format(len(records))


def test_get_request_2():
    """
    Test to verify status code returned is 200 by GET request
    Test to verify the schema
    Test to verify GET request returns only one record
    Test to verify id in response matches the input (1)
    :return: none
    """
    url = api.create_url(valid_test_url, 1)
    response = api.get_request(url, headers)
    records = [response.json()]
    assert response.status_code == 200, "TEST FAIL - Status code is NOT 200, got: {}".format(response.status_code)
    validate(instance=records, schema=schema)  # Verify schema
    print(records)  # Print for debug
    assert len(records) == 1, "TEST FAIL - GET request did NOT return only one record, got: {}".format(len(records))
    assert records[0]["id"] == 1, "TEST FAIL - id is NOT equal to 1, got: {}".format(records[0]["id"])


def test_get_response_3():
    """
    Test to verify status code returned is 404 by GET request
    Test to log the complete request and response details for troubleshooting
    :return: none
    """
    logger = logging.getLogger("my_logger")
    logger.setLevel(level=logging.DEBUG)
    response = api.get_request(invalid_test_url, headers)
    logger.debug("Response status code is: {}".format(response.status_code))
    logger.debug("Request type is: {}".format(response.request.method))
    logger.debug("Request url is: {}".format(response.request.url))
    logger.debug("Request body is: {}".format(response.request.body))
    assert response.status_code == 404, "TEST FAIL - Status code is NOT 404, got: {}".format(response.status_code)


def test_post_request():
    """
    Test to verify status code returned is 201 by POST request
    Test to verify the schema
    Test to verify the record created
    :return: none
    """
    response = api.post_request(valid_test_url, json.dumps(post_body), headers)
    records = response.json()
    assert response.status_code == 201, "TEST FAIL - Status code is NOT 201, got: {}".format(response.status_code)
    validate(instance=records, schema=schema)  # Verify schema
    print(records)  # Print for debug
    assert records["id"] == 101, "TEST FAIL - Record 101 is NOT created, got: {}".format(records["id"])


def test_put_request():
    """
    Test to verify status code returned is 200 by PUT request
    Test to verify the schema
    Test to verify record is updated
    :return: none
    """
    # Get the json before updating the record
    url = api.create_url(valid_test_url, 1)
    get_response = api.get_request(url, headers)
    get_record = get_response.json()
    # Get the json after updating the record
    url = api.create_url(valid_test_url, 1)
    put_response = api.put_request(url, put_body, headers)
    put_record = put_response.json()
    assert put_response.status_code == 200, "TEST FAIL - Status code is NOT 200, got: {}".format(put_response.status_code)
    validate(instance=put_record, schema=schema)  # Verify schema
    print(put_record)  # Print for debug
    assert put_record["title"] != get_record["title"], "TEST FAIL - Record is NOT updated"
    assert put_record["body"] != get_record["body"], "TEST FAIL - Record is NOT updated"


def test_delete_request():
    """
    Test to verify status code returned is 200 by DELETE request
    Test to verify the response
    :return: none
    """
    url = api.create_url(valid_test_url, 1)
    response = api.delete_request(url, headers)
    record = response.json()
    assert response.status_code == 200, "TEST FAIL - Status code is NOT 200, got: {}".format(response.status_code)
    assert record == {}, "TEST FAIL - Record is NOT deleted"
