#!/usr/bin/env python
__author__ = 'bing'

from httprequest import HttpRequest
from httprequesthandler import HttpRequestHandler


class Portal:
    def __init__(self):
        pass

    def create_reqeust(self):
        http_request = HttpRequest()
        return http_request

    def handle_request(self):
        http_request = self.create_reqeust()
        http_request_handler = HttpRequestHandler()
        http_response = http_request_handler.handle_request(http_request)
        print(http_response)


#for i in os.environ:
    #print '%s => %s' % (i, os.environ[i])

#print(os.environ["REQUEST_METHOD"])
#print('cookie : %s' % os.environ["HTTP_COOKIE"])

http_request = HttpRequest()
#print(http_request.field_storage)
#print(http_request.action)

#print("%s" % cgi.parse()["action"])
#print(cgi.test())



