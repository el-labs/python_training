# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + '_'.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="testname", header="testheader", footer="testfooter")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)) for i
    in range(15)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_group = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
