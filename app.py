from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.get('https://google.com.br')
# sleep(1)
element=driver.find_element(By.XPATH,"//textarea[@title='Pesquisar']")
element.click()
element.send_keys("Linux")
# sleep(1)
element.send_keys(Keys.RETURN)
assert "Linux" in driver.title

driver.close()
print('complete')
