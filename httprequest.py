#!/usr/bin/env python
__author__ = 'bing'

import os
import cgi
import cgitb

cgitb.enable(display=0, logdir=".", format="text")  # for troubleshooting


class HttpRequest:
    def __init__(self):
        self.query_string = os.environ["QUERY_STRING"]
        self.method = os.environ["REQUEST_METHOD"]
        self.cookie = os.environ["HTTP_COOKIE"]
        self.content_length = os.environ["CONTENT_LENGTH"]
        self.field_storage = cgi.FieldStorage()
        self.action = self.field_storage.getlist("action")

    def get_data_for(self, key):
        return self.field_storage.getlist(key)