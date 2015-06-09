#!/usr/bin/env python
__author__ = 'bing'

from confparser import ConfParser
from confparser import ConfException
import unittest


class TestConfParser(unittest.TestCase):
    def test_raise_exception(self):
        """An exception should be raised when html_template doesn't exist or
         when html_template is not a directory.
         """
        confparser = ConfParser("./test1_conf.txt")
        with self.assertRaises(ConfException) as excep:
            confparser.read_html_template()

        confparser = ConfParser("./test2_conf.txt")
        with self.assertRaises(ConfException) as excep:
            confparser.read_html_template()

    def test_html_template(self):
        confparser = ConfParser("./test3_conf.txt")
        res = confparser.read_html_template()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual(res["login"], "./html_template/login.html")
