# -*- coding: utf-8 -*-
from model.group import Group


def test_change_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="", header="", footer=""))
    old_groups = app.group.get_group_list()
    group = Group(name="Last1", header="Last of as1", footer="Last of nas1")
    group.id = old_groups[0].id
    app.group.change_form(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
