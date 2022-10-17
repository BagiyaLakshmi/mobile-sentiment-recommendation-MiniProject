"""
Author:Bagiya
source link: #


date:14.10.2022
last modified: 
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def write_csv(csv_path,scraped_dict,header):

    f = csv.DictWriter(open(csv_path,'a'),fieldnames=header)

    needs_header = os.stat(csv_path).st_size == 0

        # do stuff

        #if file needs a header, write headers
    if needs_header:
        f.writerow(header)
        needs_header = False

    # Then, write values
    if isinstance(scraped_dict,list):
        for i in scraped_dict:
            f.writerow(i)
    else:
        f.writerow(scraped_dict)
        




driver = webdriver.Chrome(ChromeDriverManager().install())

def get_links():
    with open('links.csv','r') as file:
        reader = csv.reader(file)
        links_list = list(reader)
    return links_list


def get_reviews(link_id):
    review_list = []
    try:
        dropdown = driver.find_element(By.XPATH,'(//span[@class="a-button-text a-declarative"])[1]').click()
        time.sleep(5)
        select= driver.find_element(By.XPATH, '//*[@id="sort-order-dropdown_1"]').click()
        for i in range(5):
            time.sleep(5)
            # dropdown.select_by_value('Most recent')
            profile_name = driver.find_elements(By.XPATH,'//span[@class="a-profile-name"]')
            date = driver.find_elements(By.XPATH,'//span[@class="a-size-base a-color-secondary review-date"]')
            reviews= driver.find_elements(By.XPATH,'//span[@class="a-size-base review-text review-text-content"]/span[1]')
            reviewers_rating = driver.find_elements(By.XPATH, '//i[@data-hook="review-star-rating"]/span[@class="a-icon-alt"]')
            print(len(reviews))
            for i in range(len(reviews)):
                review_dict = {
                    "id" : link_id,
                    "name" : profile_name[i+2].get_attribute("innerHTML"),
                    "data" : date[i+2].get_attribute("innerHTML"),
                    "reviewers_rating":reviewers_rating[1].get_attribute("innerHTML").split()[0],
                    "review" : reviews[i].get_attribute("innerHTML"),
                }
                review_list.append(review_dict)
            driver.implicitly_wait(5)
            next_page = driver.find_element(By.XPATH,'//ul[@class="a-pagination"]/li[@class="a-last"]')
            time.sleep(2)
            next_page.click()
    except Exception as e:
        print(e)
        return review_list
    else:
        return review_list

def scrap(link_id):
    try:
        title = driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
        # category =  driver.find_element(By.XPATH,'(//a[@class="a-link-normal a-color-tertiary"])[1]').text
        price = driver.find_element(By.XPATH,'(//span[@class="a-price-whole"])[5]').text
        # store=driver.find_element(By.XPATH,'//div[@class="a-section a-spacing-none"]/a').text 
        # store_new=" ".join((store.split(' '))[2:])
        rating = driver.find_element(By.XPATH,'(//span[@class="a-icon-alt"])[1]').get_attribute('innerHTML').split()[0]
        no_rating = driver.find_element(By.XPATH,'(//span[@id="acrCustomerReviewText"])[1]').text
        brand = driver.find_element(By.XPATH,'(//td[@class="a-span9"]/span[@class="a-size-base"])[1]').text
        info_dict = {
            "id" : link_id,
            # "category":category,
            "title" : title,
            "price":price,
            "brand":brand,
            # "store" : store_new,
            "rating" : rating,
            "no_rating" : no_rating,
        }
        write_csv('data_1.csv',info_dict,{"id":"id","title":"title","price":"price","brand":"brand","rating":"rating","no_rating":"no_rating"})
        time.sleep(2)

    
        # try:
        #     show_all =  driver.find_element(By.XPATH,'//*[@id="cr-pagination-footer-0"]/a')
        #     show_all.click()
        # except:
        #     show_all = driver.find_element(By.XPATH,'//a[@class="a-link-emphasis a-text-bold"]')
        #     show_all.click()
        
        # reviews = get_reviews(link_id)
        # write_csv("reviews.csv",reviews,{"id":"id","name":"name","data":"data","reviewers_rating":"reviewers_rating","review":"review"})
    
    except:
        pass   
    
if __name__ == "__main__":
    links_list = get_links()
    link_id = 544
    while(link_id<len(links_list)):
    # while(link_id<527):

        print(links_list[link_id][0])
        driver.get(links_list[link_id][0])
        scrap(link_id)
        link_id+=1




      


