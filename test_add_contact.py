# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
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
        self.create_contact(wd)
        self.create_contact_empty(wd)
        wd.find_element_by_link_text("Logout").click()

    def create_contact_empty(self, wd):
        wd.find_element_by_link_text("add next").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys("sdadasdas")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys("sadasdad")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys("asdasdas")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").send_keys("dasadad")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").send_keys("asdadsad")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").send_keys("asdasdas")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys("sadasfasdsa")
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys("asdasdas")
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").send_keys("asdasdasd")
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").send_keys("asdadsadas")
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").send_keys("adssaasddsa")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys("asdadas")
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys("asdadasdasd@sada.asd")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys("asdadasdasd@sada.asd")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys("asdadasdasdsa")
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
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("sadasdasda")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").send_keys("asdasdsa")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").send_keys("sadasdasdas")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
