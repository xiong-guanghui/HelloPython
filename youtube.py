from selenium import webdriver

driver = webdriver.chrome('c:/temp/chromedriver_win32/')
driver.fullscreen_windows()
driver.get('http://google.com')
