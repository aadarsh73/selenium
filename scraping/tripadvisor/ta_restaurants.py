from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import random as r

pd.read_csv('restaurants.csv')

chrome_driver_path = "/home/aadarsh/Development/chromedriver_linux64/chromedriver"

# "Agra", "Mumbai", "Jaipur", "Varanasi","Manali","New Delhi","Kolkata","Chennai","Shimla","Bengaluru","Ooty",

cities = ["Nainital","Darjeeling","Hyderabad","Rishikesh","Pondicherry","Gangtok","Dehradun","Leh","Ahmedabad","Srinagar","Puri","Dalhousie"]

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
    try:
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        fetch_url("https://www.tripadvisor.in/Restaurants", driver)

        driver.find_element(By.XPATH, '//*[@id="component_6"]/div/div/form/input[1]').click()
        search = driver.find_element(By.XPATH, '//*[@id="component_6"]/div/div/form/input[1]')
        search.send_keys(city)
        time.sleep(r.randint(2,5))

        # Click on the first recommendation after typing the city name
        try:
            driver.find_element(By.XPATH, '//*[@id="typeahead_results"]/a[1]').click()
        except:
            time.sleep(r.randint(2,5))
            driver.find_element(By.XPATH, '//*[@id="typeahead_results"]/a[1]').click()
        ratings = driver.find_elements(By.CSS_SELECTOR, 'span .aWhIG .LBKCf svg')
        restaurants = driver.find_elements(By.CSS_SELECTOR , '.Lwqic')

        restaurants_text = []
        ratings_text = []


        # print(ratings.get_attribute('aria-label'))
        for item in restaurants:
            restaurants_text.append(item.text)

        for item in ratings:
            ratings_text.append(item.get_attribute('aria-label'))


        print("Array Lengths ",city," :")
        print(len(restaurants_text))
        print(len(ratings_text))

        if len(restaurants_text)==0 or len(ratings_text)==0:
            print("Array Length zero for ", city, ", trying again ...")
            driver.quit()
            t= r.randint(5,10)
            print("Trying again in ", t, " seconds...")
            time.sleep(t)
            print("Fetching details for ", city, " again.")
            scraper(city)
        else:


            for i in range(len(restaurants_text)):
                try:
                    temp = {'name': [restaurants_text[i]],
                                    'rating': [ratings_text[i]],
                                    'location':[city]
                                    }
                                
                    val = pd.DataFrame(temp, columns=['name','rating','location'])
                    val.to_csv('restaurants.csv',mode='a',index=False,header=False)
                except:
                    continue

            print(city," done")

            driver.quit()
    except:
        print("error, getting", city, "again...")
        scraper(city)


for city in cities:
    scraper(city)
    t = r.randint(15,25)
    print("Getting next city in ",t, " seconds...")
    time.sleep(t)
    print("Getting next city.")
