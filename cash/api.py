#!/usr/bin/env python
import base64
from python_http_client import Client

URL_BASE = "https://free.currconv.com/api/v7"


def create_api_client():
    return Client(host=URL_BASE)

