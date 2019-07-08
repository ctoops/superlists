from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-do', self.browser.title)

        self.fail('Finish ')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
