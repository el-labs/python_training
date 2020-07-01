from model.сontact import Contact
from random import randrange


def test_all_fields_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(
            Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas",
                    nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                    home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa",
                    email="asdadas"))
        all_contacts = app.contact.get_contact_list()
        index = randrange(len(all_contacts))
        contact = all_contacts[index]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact.all_email == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
        assert contact.firstname == contact_from_edit_page.firstname
        assert contact.lastname == contact_from_edit_page.lastname
        assert contact.address == contact_from_edit_page.address
