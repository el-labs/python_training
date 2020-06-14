from model.сontact import Contact


def test_del_contact_first(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="", middlename="", lastname="",
                                       nickname="", title="", company="", address="",
                                       home="", mobile="", work="", fax="",
                                       email=""))
    app.contact.delete_first_contact()

