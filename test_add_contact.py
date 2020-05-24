# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from Contact import Contact
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        wd = self.driver
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_name("user").send_keys(Keys.DOWN)
        self.login(wd)
        self.create_contact(wd, Contact(firstname="sdadasdas", middlename="sadasdad", lastname="asdasdas", nickname="dasadad", title="asdadsad", company="asdasdas", address="sadasfasdsa",
                            home="asdasdas", mobile="asdasdasd", work="asdadsadas", fax="adssaasddsa", email="asdadas"))
        self.create_contact_empty(wd)
        wd.find_element_by_link_text("Logout").click()

    def create_contact_empty(self, wd):
        wd.find_element_by_link_text("add next").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, Contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(Contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(Contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(Contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys(Contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys(Contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(Contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(Contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys(Contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(Contact.email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("17")
        wd.find_element_by_xpath("//option[@value='17']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("//option[@value='November']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1231")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("17")
        wd.find_element_by_xpath("(//option[@value='17'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("December")
        wd.find_element_by_xpath("(//option[@value='December'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2312")
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("sadasd")
        wd.find_element_by_xpath("(//option[@value='5'])[3]").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
