import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def testNameBrowser(self):
 #       self.browser.get('http://www.google.com')
        self.assertIn('firefox', self.browser.name)

if __name__ == '__main__':
    unittest.main(verbosity=2)