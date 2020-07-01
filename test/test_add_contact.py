# -*- coding: utf-8 -*-
from model.сontact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas",
                                       nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                                       home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa",
                                       email="asdadas")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

