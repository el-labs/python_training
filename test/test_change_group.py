# -*- coding: utf-8 -*-
from model.group import Group


def test_change_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="", header="", footer=""))
    old_groups = app.group.get_group_list()
    app.group.change_form(Group(name="Last1", header="Last of as1", footer="Last of nas1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)