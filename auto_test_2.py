import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class MainTests(unittest.TestCase):
    driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
        #self.driver.get('https://www.bankmillennium.pl/logowanie')
        # title = driver.title
        # print(title)
        # assert 'Logowanie do bankowości elektronicznej - Bank Millennium' == title

    def test_demo_accounts(self):
        driver = self.driver
        driver.get('https://www.bankmillennium.pl/wniosek-o-konto-osobiste?btn_ca=01&nr=btn_ca_01&portalId=713')
        title = driver.title
        print(title)
        assert 'Wniosek o Konto Millennium 360° - Bank Millennium' == title

    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('https://www.bankmillennium.pl/bankowosc-elektroniczna/bezpieczenstwo')
        title = driver.title
        print(title)
        assert 'Bezpieczeństwo - Bank Millennium' == title


@classmethod
def tearDown(self):
    self.driver.quite()