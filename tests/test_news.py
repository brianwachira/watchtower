import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test behaviour of News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('abc-news','ABC-News','This covers every series','www.abc-news.com','business','en','us')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
