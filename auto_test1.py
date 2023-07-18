from selenium.webdriver.chrome.service import Service
from selenium import webdriver

#driver = webdriver. Chrome(executable_path='C:\TestFiles\chromedriver.exe')
driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
driver.get('https://www.bankmillennium.pl/logowanie')
title = driver.title
print(title)
assert title == 'Logowanie do bankowości elektronicznej - Bank Millennium'
driver.close()