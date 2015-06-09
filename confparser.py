#!/usr/bin/env python
__author__ = 'bing'

import os
import ConfigParser


class ConfException(Exception):
    pass


class ConfParser:
    """Define methods to read configuration information from conf.txt file."""
    def __init__(self, configuration="./conf.txt"):
        self.configuration_file = configuration

    def read_html_template(self, section="html_template"):
        """Read html template configuration information and return a dictionary object.
        :param section: section of html template configuration.
        :return: a dictionary of html template parameters.
        An ConfException will raised if can not find the corresponding section.
        """

        parser = ConfigParser.ConfigParser()
        parser.read(self.configuration_file)

        # get section, default to "html_template"
        htmls = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                htmls[item[0]] = item[1]
        else:
            raise ConfException("{0} not found in the {1} file".
                                format(section, self.configuration_file))

        if "template_dir" in htmls and htmls["template_dir"]:
            template_dir = htmls["template_dir"]

            if not os.path.isdir(template_dir):
                raise ConfException("{0} is not a directory in {1} file".
                                    format(template_dir, self.configuration_file))

            htmls.pop("template_dir")

            if "/" != template_dir[-1:]:
                template_dir += "/"

            for key in htmls:
                htmls[key] = template_dir + htmls[key]
            return htmls

    def read_db_config(self, section="mysql"):
        """ Read database configuration information and return a dictionary object.
        :param section: section of database configuration.
        :return: a dictionary of database parameters.
        An ConfException will raised if can not find the corresponding section.
        """
        # create parser and read configuration file
        parser = ConfigParser.ConfigParser()
        parser.read(self.configuration_file)

        # get section, default to mysql
        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise ConfException("{0} not found in the {1} file".format(section, self.configuration_file))
        return db

