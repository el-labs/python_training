# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Last", header="Last of as", footer="Last of nas"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


