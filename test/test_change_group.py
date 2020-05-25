# -*- coding: utf-8 -*-
from model.group import Group


def test_change_group(app):
    app.session.login(login="admin", password="secret")
    app.group.change_form(Group(name="Last1", header="Last of as1", footer="Last of nas1"))
    app.session.logout()
