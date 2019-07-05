"""
Title: API Methods
Author: Ashik Kumar
Date: 5 July 2019
"""

import requests


def create_url(url, data):
    """
    Method which creates new url from base url
    :param url: base url
    :param data: data to append to base url
    :return: new url
    """
    return url + "/" + str(data)


def get_request(url, headers):
    """
    Method which makes a GET request to specified url
    :param url: url
    :param headers: headers
    :return: get response
    """
    return requests.get(url, headers=headers)


def post_request(url, body, headers):
    """
    Method which makes a POST request to specified url
    :param url: url
    :param body: data in json format
    :param headers: headers
    :return: post response
    """
    return requests.post(url, data=body, headers=headers)


def put_request(url, body, headers):
    """
    Method which makes a PUT request to specified url
    :param url: url
    :param body: data in json format
    :param headers: headers
    :return: put response
    """
    return requests.put(url, json=body, headers=headers)


def delete_request(url, headers):
    """
    Method which makes a DELETE request to specified url
    :param url: url
    :param headers: headers
    :return: delete response
    """
    return requests.delete(url, headers=headers)
