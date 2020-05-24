# -*- coding: utf-8 -*-
from fixture.application import Application
from model.Contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create_contact(Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas",
                               nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                               home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa",
                               email="asdadas"))
    app.session.logout()