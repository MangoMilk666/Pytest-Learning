from test_project_elife.base.utils import UtilsDriver

class BasePage(object):
    def __init__(self):
        self.driver = UtilsDriver.get_driver()