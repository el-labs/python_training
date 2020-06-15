# -*- coding: utf-8 -*-
from random import randrange

from model.group import Group


def test_change_group(app):
    if app.group.count() ==0:
        app.group.create(Group(name="", header="", footer=""))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Last1", header="Last of as1", footer="Last of nas1")
    group.id = old_groups[index].id
    app.group.change_form(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
