from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
command_executor='http://localhost:4444/wd/hub',
options=options
)

driver.get('https://google.com.br')
element=driver.find_element(By.XPATH,"//textarea[@title='Pesquisar']")
element.click()
element.send_keys("Linux")
sleep(2)
element.send_keys(Keys.RETURN)
assert "Linux" in driver.title

driver.close()
print('complete')