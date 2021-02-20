#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15:29
# @Author : huangting
# @File : contact_page.py 通讯录页面
from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.hw_sele.test_pageobject.page.base_page import BasePage


class ContactPage(BasePage):
    # 跳转到添加成员页面
    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".js_add_member").click()
        from test_selenium.hw_sele.test_pageobject.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    # 跳转到添加部门页面
    def goto_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        from test_selenium.hw_sele.test_pageobject.page.add_department_page import AddDepartment
        return AddDepartment(self.driver)

    # 跳转到导入通讯录页面
    def goto_import_menber(self):
        pass

    # 返回通讯录页面的人员信息，断言
    def get_list(self):
        # find_elements拿到所有信息
        # rtype: list of WebElement
        name_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for webelement in name_webelement_list:
            name_list.append(webelement.text)
        return name_list

    # 返回通讯录页面的部门信息，断言
    def get_department_list(self):
        sleep(3)
        depart_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, '#party_name')
        # depart_webelement_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-children")
        #jstree-children
        depart_list = []
        for webelement in depart_webelement_list:
            depart_list.append(webelement.text)
        return depart_list
