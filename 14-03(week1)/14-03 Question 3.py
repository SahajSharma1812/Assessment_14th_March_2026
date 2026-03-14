
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()

sleep(3)
driver.find_element(By.ID, "name").send_keys("Sahaj Sharma")
sleep(3)
driver.find_element(By.ID, "email").send_keys("ajsahajsharma@gmail.com")
sleep(3)
driver.find_element(By.ID, "password").send_keys("Testpassword")
sleep(5)
driver.quit()