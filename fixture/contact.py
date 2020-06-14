from model.сontact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add next").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_contact_page()

    def fill_contact(self, contact):
        self.change_field_contact("firstname", contact.firstname)
        self.change_field_contact("middlename", contact.middlename)
        self.change_field_contact("lastname", contact.lastname)
        self.change_field_contact("nickname", contact.nickname)
        self.change_field_contact("title", contact.title)
        self.change_field_contact("company", contact.company)
        self.change_field_contact("address", contact.address)
        self.change_field_contact("home", contact.home)
        self.change_field_contact("mobile", contact.mobile)
        self.change_field_contact("work", contact.work)
        self.change_field_contact("fax", contact.fax)
        self.change_field_contact("email", contact.email)

    def change_field_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_contact(self, contact):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_list()
        contact = []
        for element in wd.find_elements_by_name("entry"):
            firstname = element.find_element_by_xpath(".//td[3]").text
            lastname = element.find_element_by_xpath(".//td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contact.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contact
