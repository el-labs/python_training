from model.сontact import Contact


def test_change_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="",
                                       nickname="", title="", company="", address="",
                                       home="", mobile="", work="", fax="",
                                       email=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="mmmm", middlename="mmmmm", lastname="mmmmm",
                               nickname="mmmmm", title="mmmmm", company="mmm", address="mmmm",
                               home="mmmmmm", mobile="mmmmm", work="mmmmmm", fax="mmmm",
                               email="mmmmmmmmm")
    contact.id = old_contacts[0].id
    app.contact.change_contact(contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

