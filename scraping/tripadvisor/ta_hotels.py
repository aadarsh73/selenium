from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd
import random as r

pd.read_csv('hotels.csv')

chrome_driver_path = "/home/aadarsh/Development/chromedriver_linux64/chromedriver"

cities = ["Agra", "Mumbai", "Jaipur", "Varanasi","Manali","New Delhi","Kolkata","Chennai","Shimla","Bengaluru","Ooty","Nainital","Darjeeling","Hyderabad","Rishikesh","Pondicherry","Gangtok","Dehradun","Leh","Ahmedabad","Srinagar","Puri","Dalhousie"]


def fetch_url(url, driver):
    try:
        print("fetching url...")
        return driver.get(url)
        print("url fetched successfully!")
    except:
        t = r.randint(5,10)
        print("Error, retrying in ",t," seconds...")
        time.sleep(t)
        fetch_url(url, driver)


def scraper(city): 
    global chrome_driver_path
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    fetch_url("https://www.tripadvisor.in", driver)
    driver.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[1]/div/div/div[1]/a').click()
    time.sleep(r.randint(3,6))
    # driver.find_element(By.XPATH, '/html/body/div[4]/div/form/input[1]').click()
    try:
        search = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/input[1]')
    except:
        try:
            search = driver.find_element(By.XPATH, '/html/body/div[2]/div/form/input[1]')
        except:
            try:
                search = driver.find_element(By.XPATH, '/html/body/div[3]/div/form/input[1]')
            except:
                search = driver.find_element(By.XPATH, '/html/body/div[4]/div/form/input[1]')
        
    search.send_keys(city)
    time.sleep(r.randint(2,5))

    # Click on the first recommendation after typing the city name
    driver.find_element(By.XPATH, '//*[@id="typeahead_results"]/a[1]').click()
    time.sleep(r.randint(2,5))

    # Enter check-in dates
    # driver.find_element(By.XPATH, '//*[@id="PERSISTENT_TRIP_SEARCH_BAR"]/div[1]/div/div/div[1]/button[1]/div').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[5]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[4]/div[5]/div').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[5]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[4]/div[6]/div').click()
    # driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[5]/div[2]/div/div[2]/div/div[4]/button').click()

    # Getting and storing hotel names

    try:
        driver.find_element(By.XPATH, '//*[@id="component_3"]/div/button').click()
    except:
        pass
        
    hotels = driver.find_elements(By.CSS_SELECTOR, '.ui_column div .prw_rup .listing_title .property_title')
    try:
        prices = driver.find_elements(By.CSS_SELECTOR, '.priceBlock .price-wrap .price')
    except:
        prices = driver.find_elements(By.CSS_SELECTOR, '.priceBlock .price-wrap div')

    reviews = driver.find_elements(By.CSS_SELECTOR, '.ui_bubble_rating')
    reviews_text = []
    hotels_text = []
    price_text = []
    for item in reviews:
        reviews_text.append(item.get_attribute('alt'))
    for item in hotels:
        hotels_text.append(item.text)
    for item in prices:
        price_text.append(item.text)
    print("Array Lengths ",city," :")
    print(len(reviews_text))
    print(len(hotels_text))
    print(len(price_text))

    if len(hotels_text)==0 or len(reviews_text)==0 or len(price_text)==0:
        print("Array Length zero for ", city, ", trying again ...")
        driver.quit()
        t= r.randint(5,10)
        print("Trying again in ", t, " seconds...")
        time.sleep(t)
        print("Fetching details for ", city, " again.")
        scraper(city)
    else:
        # print("Hotesl and prices")
        # print(hotels_text)
        # print(price_text)
        # print(reviews_text)

        for i in range(len(hotels_text)):
            temp = {'Hotel': [hotels_text[i]],
                            'Price': [price_text[i]],
                            'Review':[reviews_text[i]],
                            'Location':[city]
                            }
                        
            val = pd.DataFrame(temp, columns=['Hotel', 'Price', 'Review', 'Location'])
            val.to_csv('hotels.csv',mode='a',index=False,header=False)

        print(city," done")

        driver.quit()

for city in cities:
    scraper(city)
    t = r.randint(15,25)
    print("Getting next city in ",t, " seconds...")
    time.sleep(t)
    print("Getting next city.")



