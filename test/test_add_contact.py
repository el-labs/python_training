# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas",
                                       nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                                       home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa",
                                       email="asdadas"))


def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", middlename="", lastname="",
                                       nickname="", title="", company="", address="",
                                       home="", mobile="", work="", fax="",
                                       email=""))
