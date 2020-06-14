from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

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
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def change_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))
