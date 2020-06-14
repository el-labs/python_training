from model.сontact import Contact


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create_contact(Contact(firstname="1234", middlename="123123", lastname="12313",
                               nickname="1231", title="1323", company="3123", address="1312",
                               home="132", mobile="13", work="312", fax="13",
                               email="13"))
    app.session.logout()
