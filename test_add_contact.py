# -*- coding: utf-8 -*-
from application import Application
from Contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas",
                               nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                               home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa",
                               email="asdadas"))
    app.logout()
