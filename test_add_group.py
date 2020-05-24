# -*- coding: utf-8 -*-
from application import Application
from group import Group
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(login="admin", password="secret")
        self.app.create_group(Group(name="Last", header="Last of as", footer="Last of nas"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(login="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
