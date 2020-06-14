from model.сontact import Contact


def test_change_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="",
                                       nickname="", title="", company="", address="",
                                       home="", mobile="", work="", fax="",
                                       email=""))
    app.contact.change_contact(Contact(firstname="mmmm", middlename="mmmmm", lastname="mmmmm",
                               nickname="mmmmm", title="mmmmm", company="mmm", address="mmmm",
                               home="mmmmmm", mobile="mmmmm", work="mmmmmm", fax="mmmm",
                               email="mmmmmmmmm"))
