from password import *


import selenium
from selenium import webdriver
#inconspicuous code: document.querySelector('div[role=dialog] ul').parentNode.scrollBy(0,100)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from time import sleep
import os

"""
camel case for variables
Pascal Case for classses
underscores for functions

camelCase
PascalCase
under_score
"""

#options = webdriver.ChromeOptions()
#options.add_argument('headless') , options=options

driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.instagram.com")


class Element:
        # A simple class to manage Selenium Elements
        xpath = ""
        driver = ""
        def __init__(self, target_driver, xpath):
                self.xpath = xpath
                self.driver = target_driver


        def wait_until_loaded(self):
                # Used before finding an element. Determines whether it is there in the screen
                delay = 1.5 # seconds
                try:
                        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, self.xpath)))
                except TimeoutException:
                        print("Took Too Much Time To Load")
                        quit()
                        
        def click(self):
                # Simulates a click through selenium
                self.driver.find_element_by_xpath(self.xpath).click()

        def send_keys(self, keys):
                # Sends keys into a element through selenium
                self.driver.find_element_by_xpath(self.xpath).send_keys(keys)

        def get_text(self):
                #Retrieves the innerHTML from an element, usually the text
                return self.driver.find_element_by_xpath(self.xpath).text

        
#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input

# Inputs The Username Into The Username Textbox
usernameTextbox = Element(driver, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
usernameTextbox.wait_until_loaded()
usernameTextbox.send_keys(USERNAME)
 
# Inputs the Password Into The Password Textbox
passwordTextbox = Element(driver, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input" )
passwordTextbox.wait_until_loaded()
passwordTextbox.send_keys(PASSWORD)

#Clicks The "Sign In" Button To Sign In
signinButton = Element(driver, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
signinButton.wait_until_loaded()
signinButton.click()  


sleep(10) # Wait 5 Seconds For The Page To load
driver.get("http://instagram.com/{}".format(USERNAME))

# Finds The Button To Go Into The "Followers" Screen
followersButton = Element(driver, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a") 
followersButton.wait_until_loaded()
followersButton.click()
sleep(2.5)



#Initialized Three empty lists to get the usernames, display names, and status of each person

#usernames = []
#display_names = []
#statuses = [] # Status can be either following or follow: 

# Following means we are both following eachother while Follow means only they are following me
all_names = []
followerNumber = 1
# if f%3 == 1   the text is the username
# if f%3 == 2   the text is the display name
#  if f%3 == 0  the text is the status
while True:
        try: 
                driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollBy(0,100)")
                css_selector = "body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({})".format(followerNumber)
                followerElement = driver.find_element_by_css_selector(css_selector)
                followerName = followerElement.text

                all_names.append(followerName)
                """
                if (followerNumber % 3) == 1:
                        usernames.append(followerName)
                elif (followerNumber % 3 )== 2:
                        display_names.append(followerName)
                elif (followerNumber % 3)== 0:
                        statuses.append(followerName.replace("\n", ""))
                """
                # do the check whether its uname display name or status
                

                followerNumber += 1
        except selenium.common.exceptions.NoSuchElementException:
                break

# Creates list of accounts that you follow from followers      
username_list = []

for i in range(len(all_names)):
        if "Following" in all_names[i]:
                split_string = all_names[i].split("\n", 1)
                username_string = split_string[0]
                username_list.append(username_string)
                

for i in username_list:
        print(i)


# Same code but for following tab instead


# Goes to profile page

sleep(5)

driver.get("http://instagram.com/{}/".format(USERNAME))



# Finds the button to go into the "Following" screen
sleep(5)
followingButton = Element(driver, "//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[3]/a")
followingButton.wait_until_loaded()
followingButton.click()

following_names = []
followingNumber = 1

sleep(5)
while True:
        #body > div.RnEpo.Yx5HN > div > div > div.isgrP
        try: 
                # Tells selenium to run js
                # document
                driver.execute_script("document.querySelector('div[role=dialog] ul').parentNode.scrollBy(0,100)")

                css_selector = "body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({})".format(followingNumber)
                followingElement = driver.find_element_by_css_selector(css_selector)
                followingName = followingElement.text

                following_names.append(followingName)
                followingNumber += 1
        except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.JavascriptException) as error:
                #print(error)
                break

# list of all usernames that are followed
following_username_list = []

for i in range(len(following_names)):
        if "Following" in following_names[i]:
                split_string = following_names[i].split("\n", 1)
                username_string = split_string[0]
                following_username_list.append(username_string)

for i in following_username_list:
        print(i)

not_following_back = [i for i in following_username_list if i not in username_list]
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(not_following_back)
# people

#  //*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a

"""
followingButton = Element(driver, "//*[@id=\"react-root\"]/section/main/div/ul/li[3]/a")
followingButton.wait_until_loaded()
followingButton.click()
"""

"""
potato = ["loser", "loser", "not_loser"]

# Iterate through potato list, if i == "loser", append i to new_potato list
new_potato = [i if i == "loser" for i in potato]

last = [i if i not in following for i in followers]
"""