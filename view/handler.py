#!/usr/bin/env python
__author__ = 'bing'

from viewgenerator import ViewGenerator
from confparser import ConfParser
from user.usermanager import UserManager
from user.usermanager import User


class HandlerException:
    """ViewException stands for Exception occurring when reading html pages."""
    pass


class BaseHandler:
    """BaseHandler reads content of html files specified by file_name"""
    def __init__(self):

        self.viewgenerator = ViewGenerator()
        self.confparser = ConfParser()

        self.response_types = {
            "text": "Content-type:text/html\n"
        }

    def handle(self, http_request, http_response):
        pass

    def _error_(self, http_request, http_response):
        http_response.add_header(self.response_types["text"])
        http_response.add_content(
            self.viewgenerator.read_page(
                "error_page",
                "error_page",
                None
            )
        )
        return http_response


class ErrorPageHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    def handle(self, http_request, http_response):
        return self._error_(http_request, http_response)


class LoginHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.file_name = "login_page"
        self.section_name = "login_page"

    def handle(self, http_request, http_response):
        """Once called,Return login html file."""
        http_response.add_header(self.response_types["text"])
        http_response.add_content(
            self.viewgenerator.read_page(
                self.file_name,
                self.section_name
            )
        )
        return http_response


class RegisterHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.file_name = "register_page"
        self.section_name = "register_page"

    def handle(self, http_request, http_response):
        http_response.add_header(self.response_types["text"])
        http_response.add_content(
            self.viewgenerator.read_page(
                self.file_name,
                self.section_name
            )
        )
        return http_response


class AuthenticateHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.usermanager = UserManager()

    def handle(self, http_request, http_response):
        """Check whether user name and password are correct or not."""
        http_response.add_header(self.response_types["text"])

        login_section = self.confparser.read_section(section="login_page")
        name = http_request.get_data_for(login_section["login_name"])
        password = http_request.get_data_for(login_section["login_password"])
        user = User(name, password)

        errors = {
            "error1": "Name can not be empty.",
            "error2": "Password can not be empty.",
            "error3": "Name or Password is not correct."
        }

        error = ""
        if name is None or "" == name.strip():
            error = "error1"
        elif password is None or "" == password.strip():
            error = "error2"
        elif not self.usermanager.authenticate(user):
            error = "error3"

        if "" != error:
            login_section["login_error"] = errors[error]
            http_response.add_content(
                self.viewgenerator.read_page(
                    "login_page",
                    "login_page",
                    login_section
                )
            )
            return http_response

        http_response.add_content(
            self.viewgenerator.read_page(
                "main_page",
                "main_page",
                None
            )
        )
        return http_response


class CreateNewUserHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.usermanager = UserManager()

    def handle(self, http_request, http_response):
        """Create a new user acount."""
        http_response.add_header(self.response_types["text"])

        register_section = self.confparser.read_section(section="register_page")
        name = http_request.get_data_for(register_section["register_name"])
        first_pass = http_request.get_data_for(register_section["register_first_password"])
        second_pass = http_request.get_data_for(register_section["register_second_password"])

        errors = {
            "error1": "Name can not be empty.",
            "error2": "First password can not be empty.",
            "error3": "Second password can not be empty.",
            "error4": "The passwords are not the same."
        }

        error = ""
        if name is None or "" == name.strip():
            error = "error1"
        elif first_pass is None or "" == first_pass.strip():
            error = "error2"
        elif second_pass is None or "" == second_pass.strip():
            error = "error3"
        elif first_pass != second_pass:
            error = "error4"

        user = User(name, first_pass)

        if "" != error:
            register_section["register_error"] = errors[error]
            http_response.add_content(
                self.viewgenerator.read_page(
                    "register_page",
                    "register_page",
                    register_section
                )
            )
            return http_response

        if not self.usermanager.create_new_user(user):
            register_section["register_error"] = self.usermanager.error
            http_response.add_content(
                self.viewgenerator.read_page(
                    "register_page",
                    "register_page",
                    register_section
                )
            )
            return http_response

        http_response.add_content(
            self.viewgenerator.read_page(
                "main_page",
                "main_page",
                None
            )
        )
        return http_response


class UploadPageHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    def handle(self, http_request, http_response):
        http_response.add_header(self.response_types["text"])
        http_response.add_content(
            self.viewgenerator.read_page(
                "upload_page",
                "upload_page",
                None
            )
        )
        return http_response


class LogoutHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    def handle(self, http_request, http_response):
        pass


class UploadImageFileHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    def handle(self, http_request, http_response):
        pass


class CheckImageFileHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    def handle(self, http_request, http_response):
        pass