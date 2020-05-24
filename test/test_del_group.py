

def test_del_group_first(app):
    app.session.login(login="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()