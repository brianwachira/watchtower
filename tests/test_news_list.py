import unittest
from app.models import News_List


class News_ListTest(unittest.TestCase):
    '''
    Test Class to test behaviour of News_list class
    '''

    def setUp(self):
        '''
        Set up method that runs before every Test
        '''
        self.new_news_list = News_List('branham','A Week Later','loerm ipsum ipsum lorem','http://www.abc.com','http://www.bca.com','kmart','lorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsumlorem ipsum ipsum ipsum ipsum ipsum')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_list,News_List))