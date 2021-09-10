# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:58:08 2020

"""
def scroll_down():
    #SCROLL DOWN TO BOTTOM OF THE PAGE#
    time.sleep(0.5)
    
    SCROLL_PAUSE_TIME = 0.5
    
    # Get scroll height
    last_height = dub.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to bottom
        dub.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = dub.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def sleep():
    time.sleep(3)

def Bqool_Login():
    
    try:
       lnk="https://acc.bqool.com/public/logout"
       dub.get(lnk)        
    except:
        pass
           
    lnk = (f'https://acc.bqool.com/login') 
    dub.get(lnk)
    
    email = 'censored@gmail.com'
    password = 'censored'
    
    css_l = dub.find_elements_by_css_selector
    css = dub.find_element_by_css_selector
    
    try:  #Try to type Email  
        acc_field = css_l('div[class="input_box"]')
        for each in acc_field:
            try:
                email_css = each.find_element_by_id('EMail')
                email_css.clear()
                email_css.click()
                email_css.send_keys(str(email))
            except:
                continue    
    except:
        pass
    
    try:  #Try to type Password  
        acc_field = css_l('div[class="input_box"]')
        for each in acc_field:
            try:
                pass_css = each.find_element_by_id('PWD')
                pass_css.click()               
                pass_css.send_keys(str(password))
            except:
                continue    
    except:
        pass    
    
# =============================================================================
#     already_checked = dub.find_element_by_css_selector('p[class="box02 flex condition"]')
#     try:
#         already_checked.find_element_by_css_selector('input[value="true"]')
#         checked = True    
#     except:
#         checked = False
#     
#     if checked != True:
#         keep_signed = css('label[for="login-check"]')
#         keep_signed.click()     #No css signal if clicked or not
# =============================================================================
    
    sign_in = css('a[id="login"]')
    sign_in.click()

def Bqool_Uploader(upload_file):
    
    upload_file = upload_file.replace('/','\\') + 'bqool_inv_file.txt'

    
    options = webdriver.ChromeOptions() 
    options.add_argument(r'user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default'.format(str(os.getenv('username'))))
    global dub
    dub = webdriver.Chrome(executable_path="chromedriver.exe")#, options=options)
    dub.implicitly_wait(1)   
    
    dub.set_window_size(1080, 1080)
    dub.set_window_position(-5,0, windowHandle='current')
    #dub.maximize_window()
    
    Bqool_Login()
    
    lnk = 'https://mc.bqool.com/repricing/amazonus/upload'
    dub.get(lnk)
    sleep()
    
    
    upload_box = WebDriverWait(dub, 3).until(
                        EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'form[action="/repricing/amazonus/upload"]')))
    dd_choose_file_type = upload_box.find_element_by_css_selector('span[class="t-select"]')
    dd_choose_file_type.click()
    
    
    file_types_menu = WebDriverWait(dub, 3).until(
                        EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class="t-animation-container"]')))
    file_types = file_types_menu.find_elements_by_xpath('//li')
    for each in file_types:
        if 'Repricing Central File' in each.text:
            each.click()
            sleep()
        else: continue
    
    #Choose file button
    file_input_btn = upload_box.find_elements_by_css_selector('table[class="normal"]')
    file_input_btn = file_input_btn[1]
    file_input_btn.click()
    sleep()
    
    pyautogui.typewrite(upload_file)
    pyautogui.press('enter')
    sleep()
    
    upload_button = WebDriverWait(dub, 3).until(
                        EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'input[class="button_save')))
    upload_button.click()
    time.sleep(5)

    
    sleep()
    dub.quit()

#-----------------------------------------------------------------------------#

import pyautogui
import time
import os

from selenium                                import webdriver
from selenium.webdriver.common.by            import By
from selenium.webdriver.support.ui           import WebDriverWait
from selenium.webdriver.support              import expected_conditions as EC


    
if __name__ == "__main__":
    #Bqool upload file location
    upload_file = r'C:\Users\CoilingDragon\Desktop\Python\upl_inv_to_amz\bqool_inv_file.txt'
    Bqool_Uploader(upload_file)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    