#!/usr/bin/env python
__author__ = 'bing'


class HttpResponse:
    """HttpResponse contains http response headers and body content."""
    header_end = "\n"

    def __init__(self):
        self.headers = []
        self.content = None
        self.response = None

    def add_header(self, header):
        self.headers.append(header)

    def add_content(self, content):
        self.content = content

    def __str__(self):
        for header in self.headers:
            self.response += header
        self.response += self.data
        return self.response