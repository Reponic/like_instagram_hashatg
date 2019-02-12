from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter
from tkinter import StringVar
from tkinter import *
##import json

class InstaHelp: 

    def __init__(self):

        ##Setting up Tkinter and Variables
        self.root = Tk()
        self.hashtag = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        ##Button to action
        self.Button_Like = Button(self.root, text="Like Hashtag", command=self.like_photo)

        ##Text Box For Hashtag
        self.Entry_LikeHashatg = Entry(self.root, textvariable=self.hashtag)
        self.Entry_LikeHashatg.insert(0, 'Hashtag To Like')

        #Text Box for Username and Pasword.
        self.Entry_Username = Entry(self.root, textvariable=self.username)
        self.Entry_Username.insert(0, 'Username')
        self.Entry_Password = Entry(self.root, textvariable=self.password, show="*")
        self.Entry_Password.insert(0, 'Password')

        ##Packing all into the windows to be shown.
        self.Button_Like.pack()
        self.Entry_LikeHashatg.pack()
        self.Entry_Username.pack()
        self.Entry_Password.pack()

        ##Setting Up the driver (Selenium).
        self.driver = webdriver.Firefox()
        
       
    def closeBrowser(self) :
        self.driver.close()

    def openWindow(self):
        self.root.mainloop()

    def login(self) :
        ##Getting the Username and the Password
        PW = str(self.password.get())
        UN = str(self.username.get())

        ##Setting up driver variable.
        driver = self.driver

        #Where the fun beggins

        ##Getting Website
        driver.get('https://www.instagram.com/')
        time.sleep(2)

        ##Locating loggin Button and clicking on it
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)

        ##Locating Input elements for Username and Password and Populating them

        ##Username
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(UN)

        ##Password
        password_elem =  driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(PW)

        ##Simulating Enter Key
        password_elem.send_keys(Keys.RETURN)
        time.sleep(4)
    
    def like_photo(self) :

        ## Action the Login Function
        self.login()

        driver = self.driver

        ## New
        hashtag =str(self.hashtag.get())
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(2)
        for i in range (1,8):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        hrefs = driver.find_elements_by_xpath('/html/body/span/section/main/article/div/div/div/div/div/a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        print(hashtag + ' photos: '+ str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                time.sleep(4)
                like_button = lambda: driver.find_element_by_xpath("//span[@aria-label='Like']")
                like_button().click()
                time.sleep(4)
            except Exception as e:
                print(e)
                time.sleep(2)
        
        driver.close()
            

IB = InstaHelp()
IB.openWindow()