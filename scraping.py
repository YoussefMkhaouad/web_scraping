import selenium
from selenium import webdriver
import pandas as pd

from selenium.webdriver.common.keys import Keys
import os
import time
import csv
import re

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument('--ignore-certificate-errors')

browser = webdriver.Chrome(executable_path='C:/Users/Mkhaouad/Documents/chromedriver', options= option)

def autoscout():

    #Define the url and access it
    url = "https://www.autoscout24.com/lst/volkswagen/golf-(all)?sort=price&desc=0&ustate=N%2CU&kmto=50000&fregfrom=2016&atype=C&ac=0"
    browser.get(url)
    time.sleep(2)

    #Create list of URLs we need to open
    i = 2
    url_list = []

    #We already add the first URL to the list
    url_list.append(url)

    #Iterate in order to create URls
    while i < 4:

        url_to_add = "https://www.autoscout24.com/lst/volkswagen/golf-(all)?sort=price&desc=0&ustate=N%2CU&size=20&page=" + str(i) + "&kmto=50000&fregfrom=2016&atype=C&ac=0&"
        url_list.append(url_to_add)
        i += 1

    #Print the resulting list
    print(url_list)

    #Create blank frame - this is where we add the data we scrap
    listing_frame = pd.DataFrame(columns=["listing"])

    #First loop: we iterate over the different webpages we created previously
    for webpage in url_list:

        #We open the page
        browser.get(webpage)

        #On the webpage that is currently open, we create a list of all the listings
        listings = browser.find_elements_by_xpath("//*[@class = 'cl-list-elements']//*[@class='cldt-summary-full-item-main']")

        #Second loop: we iterate over the listings in order to find each listing's details
        for listing in listings:

            #Extract the text from each listing
            listing_data = listing.text

            #Create a dictionary
            listing_data = {"listing": listing_data}

            #Add dictionary to a dataframe
            with open('employee_file2.csv', mode='w') as csv_file:

            	fieldnames = ['listing']
            	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            	writer.writeheader()
            	for row in listing_data:
            		writer.writerow({'listing':row})

            #Wait time
            time.sleep(1)

            #Print frame (Work in progress)

    #Print final main frame

    #Our taks is exectued, we quit the browser
    browser.quit()

#excute the function
autoscout()