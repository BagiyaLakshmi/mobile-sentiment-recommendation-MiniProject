from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
import csv
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager



# load_dotenv()

# PATH=os.environ.get('PATH')

driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get("https://www.amazon.in/")

driver.maximize_window()

total_mobiles_links=[]

#Loop through the every link in the list
def links():

    len_link=len(total_mobiles_links)

    for i in range(0,len_link):

        single_link=total_mobiles_links[i]

        # print (i)

        driver.get(single_link)

    # print(total_mobiles_links)



def startpy():
    
    count = 0



    search=driver.find_element_by_id('twotabsearchtextbox')

    search.send_keys('mobile phones')
    search.send_keys(Keys.RETURN)

    while True:

        mobiles=driver.find_elements_by_xpath("//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

        #Collect every links for the page and store the links in total_mobile_links
        for mobile in mobiles:

            det=mobile.get_attribute('href')
            count = count + 1

            print(count)

            total_mobiles_links.append(det)

        df = pd.DataFrame(total_mobiles_links)
        if os.stat("links.csv").st_size == 0:
            df.to_csv('links.csv', mode='a', index=False, header=True)
        else:
            df.to_csv('links.csv', mode='a', index=False, header=False)


        driver.implicitly_wait(5)
        next_page= driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]').click()
        time.sleep(2)

        
    # print(total_mobiles_links)



if __name__=='__main__':

    startpy()