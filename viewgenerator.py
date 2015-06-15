#!/usr/bin/env python
__author__ = 'bing'

import sys
from string import Template
from confparser import ConfException
from confparser import ConfParser


class ViewGenerator:
    default_error_file = "./default_error/default_error.html"

    def __init__(self):
        self.htmls = {}
        try:
            confparser = ConfParser()
            self.htmls = confparser.read_html_template()
        except ConfException as cex:
            sys.stderr.writelines(cex)

        # if a customized error file is not provided, use the default one.
        if "error_page" not in self.htmls or self.htmls["error_page"] is None\
                or "" == self.htmls["error_page"]:
            self.htmls["error_page"] = self.default_error_file

        self.get_pages = {
            "login_page": lambda: self._read_page_("login_page", "login_page"),
            "register_page": lambda: self._read_page_("register_page", "register_page"),
            "error_page": lambda: self._read_page_("error_page", "error_page")
        }

    def _read_page_(self, file_name, section_name):
        with open(self.htmls[file_name]) as f:
            file_content = f.read()
        confparser = ConfParser()
        template = Template(file_content)
        return template.substitute(confparser.read_section(section=section_name))