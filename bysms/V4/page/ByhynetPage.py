#byhy.net网页的page
from selenium.webdriver.common.by import By

from V4.base.page_base import BasePage

class ByhyPage(BasePage):
    def find_teaching_btns(self): #find_elements 返回一个列表
        return self.driver.find_elements(By.CSS_SELECTOR, "div.topic-list:nth-child(2)>a")
class ByhyHandle:
    def __init__(self):
        self.page = ByhyPage()
    def get_teaching_sessions(self):
        contents = []
        for i in range(18):
            contents.append(self.page.find_teaching_btns()[i].text)
        return contents
