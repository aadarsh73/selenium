from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/home/aadarsh/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.tripadvisor.in/CheapFlightsHome")

to = 'New Delhi'
fro = 'Bangalore'

origin= driver.find_element(By.XPATH, '//*[@id="taplc_trip_search_home_flights_0"]/div[2]/div/span/div[1]/div[2]/div[1]/div/div[1]/input[2]').click()
origin= driver.find_element(By.XPATH, '//*[@id="taplc_trip_search_home_flights_0"]/div[2]/div/span/div[1]/div[2]/div[1]/div/div[1]/input[2]').click()
origin.send_keys(fro)
driver.find_element(By.XPATH,'//*[@id="react-autowhatever-fsc-origin-search--item-0"]').click()
driver.find_element(By.CSS_SELECTOR, '.ui_typehead_results').click()

# origin.send_keys(fro)


# driver.find_element(By.XPATH, '//*[@id="typeahead_results"]/a[1]/div[2]').click()
# time.sleep(15)
# try:
#     driver.find_element(By.XPATH,'//*[@id="component_3"]/div/button').click()
# except: 
#     pass
# driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[1]/button').click()
# driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[5]/div[7]/div').click()
# driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div[6]/div[1]/div')
# time.sleep(5)
# hotels = driver.find_elements(By.CSS_SELECTOR, '.listing_title .property_title')
# prices = driver.find_elements(By.CSS_SELECTOR, 'vjPLw vXCuD biGQs fwoto span')
# for item in hotels:
#     print(item.text)
# for item in prices:
#     print(item.text)

driver.quit()


