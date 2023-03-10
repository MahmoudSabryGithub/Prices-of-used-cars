# Importing required libraries
import requests
from bs4 import BeautifulSoup
from pandas import *
import csv

# Getting number of pages for search
pages_range=input("Inter range of pages for search:")
full_details = []


# Looping over each page
for number_of_page in range(int(pages_range)):
    # Get connect with source page
    page = requests.get("https://www.olx.com.eg/en/vehicles/cars-for-sale/?page=" + str(number_of_page))

    #Extracting cars from page
    def details(page):
        src = page.content
        soup = BeautifulSoup(src, "lxml")
        cars = soup.find_all("li", {"class": "c46f3bfe"})

        #Extracting each car details
        def car_detail(cars):
            car_name = cars.contents[0].find("div", {"class": "a5112ca8"}).text.strip()
            car_price = cars.contents[0].find("span", {"class": "_95eae7db"}).text.strip()
            car_model = cars.contents[0].find("span", {"class": "c47715cd"}).text.strip()
            car_usage = cars.contents[0].find("span", {"class": "fef55ec1"}).find("span",
                                                                                  {"class": "fef55ec1"}).text.strip()
            car_location = cars.contents[0].find("span", {"class": "_424bf2a8"}).text.strip()
            full_details.append({"Car name": car_name, "Car price": car_price, "Model": car_model, "Usage": car_usage,
                                 "Location": car_location})

        for i in range(len(cars)):
            car_detail(cars[i])


    details(page)

# Creating Data frame of the resulted data
data = DataFrame(full_details)
print(data)

# Transforming data frame to excel file
data.to_excel("C:\\Users\\DELL\\Documents\\Python\\Scraping using python\\2.xlsx")

