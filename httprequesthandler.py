#!/usr/bin/env python
__author__ = 'bing'

from httpreponse import HttpResponse
from viewgenerator import ViewGenerator


class HttpRequestHandler:
    """handle http request,return http response."""
    def __init__(self):
        """Record each handler for each HttpRequest.action."""
        self.view_generator = ViewGenerator()
        self.handlers = {
            "login": lambda: self._get_login_page_(),
            "register": lambda: self._get_register_page_(),
            "authenticate": lambda: self._authenticate_(),
            "create_new_user": lambda: self._create_new_user_()
        }
        self.http_version = "HTTP/1.1"
        self.response_types = {
            "text": "Content-type:text/html\n"
        }
        self.responses = {
            200: " 200 Ok\n",
            404: " 404 Not found\n"
        }

    def handle_request(self, http_request):
        action = http_request.action
        # to do: error handler
        if action in self.handlers:
            return self.handlers[action]()
        else:
            return self._get_error_page_()

    def do_get(self):
        content = "<html><body>Path is: %s</body></html>" % self.path
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-length', str(len(content)))

        #cookie = Cookie.SimpleCookie()
        #cookie['id'] = 'some_value_42'

        #self.wfile.write(cookie.output())
        self.wfile.write('\r\n')

        self.end_headers()
        self.wfile.write(content)

    def _get_login_page_(self):
        """Once called,Return login html file."""
        http_response = HttpResponse()
        #http_response.add_status_code(self.http_version+self.responses[200])
        http_response.add_header(self.response_types["text"])
        http_response.add_content(self.view_generator.get_pages["login_page"]())
        return http_response

    def _get_register_page_(self):
        http_response = HttpResponse()
        http_response.add_header(self.response_types["text"])
        http_response.add_content(self.view_generator.get_pages["register_page"]())
        return http_response

    def _authenticate_(self):
        """Check whether user name and password are correct or not."""
        pass

    def _create_new_user_(self):
        """Create a new user acount."""
        pass

    def _get_error_page_(self):
        http_response = HttpResponse()
        #http_response.add_status_code(self.http_version+self.responses[202])
        http_response.add_header(self.response_types["text"])
        http_response.add_content(self.view_generator.get_pages["error_page"]())
        return http_response
