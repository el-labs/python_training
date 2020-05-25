# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create_contact(Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas",
                               nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                               home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa",
                               email="asdadas"))
    app.session.logout()
