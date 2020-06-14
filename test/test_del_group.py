from model.group import Group


def test_del_group_first(app):
    if app.group.count() == 0:
        app.group.create_contact(Group(name="", header="", footer=""))
    app.group.delete_first_group()
