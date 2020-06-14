from model.сontact import Contact


def test_change_contact(app):
    app.contact.change_contact(Contact(firstname="mmmm", middlename="mmmmm", lastname="mmmmm",
                               nickname="mmmmm", title="mmmmm", company="mmm", address="mmmm",
                               home="mmmmmm", mobile="mmmmm", work="mmmmmm", fax="mmmm",
                               email="mmmmmmmmm"))
