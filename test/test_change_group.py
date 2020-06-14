# -*- coding: utf-8 -*-
from model.group import Group


def test_change_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="", header="", footer=""))
    app.group.change_form(Group(name="Last1", header="Last of as1", footer="Last of nas1"))

