#!/usr/bin/env python
__author__ = 'bing'


class User:
    def __init__(self, name, passwd):
        self.name = name
        self.password = passwd


class UserManager:
    """UserManger is responsible for authenticating user informaiton or
    creating a new user in database.
    """
    def __init__(self):
        """
        error contains the corresponding error messsage.
        """
        self.error = ""

    def authenticate(self, user):
        # TODO
        return True

    def create_new_user(self, user):
        # TODO
        return True
