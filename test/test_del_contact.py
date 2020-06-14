

def test_del_contact_first(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
