from V4.base.utils import UtilsDriver

class BasePage(object):
    '''
    'object' is used to referring create a new-style class in Python.
    optional in python3
    '''

    def __init__(self):
        self.driver = UtilsDriver.get_driver()