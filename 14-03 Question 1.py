from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.facebook.com")

driver.find_element(By.CSS_SELECTOR, "input#_R_1h6kqsqppb6amH1_").send_keys("Sahaj ")
driver.find_element(By.CSS_SELECTOR, "input#_R_1hmkqsqppb6amH1_").send_keys("Sharma")
driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"').click()