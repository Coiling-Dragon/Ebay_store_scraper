# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:16:27 2020

"""

def Amazon_Uploader(upload_file):
    upload_file = upload_file.replace('/','\\') + 'amazon_inv_file.txt'

    
    options = webdriver.ChromeOptions() 
    options.add_argument(r'user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default'.format(str(os.getenv('username'))))
    global du
    du = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    du.implicitly_wait(1)   
    
    du.set_window_size(1080, 1080)
    du.set_window_position(-5,0, windowHandle='current')
    
    #du.maximize_window()
    
    AZ_login(du)
    
    lnk = 'https://sellercentral.amazon.com/listing/upload?ref_=xx_upload_tnav_download'
    du.get(lnk)
    time.sleep(3)
    
    dd_filetype = WebDriverWait(du, 3).until(
                        EC.presence_of_element_located(
                        (By.ID, 'a-autoid-2-announce')))
    dd_filetype.click()
    
    dd_list = du.find_elements_by_css_selector('li[role="option"]')
    for each in dd_list:          #locate drop-down
        if 'Price & Quantity File' in each.text:
            each.click()
            time.sleep(3)
        else:
            continue
    
    scroll_down()
    
    #Page upload canvas (Bottom Box)
    page_upload_canvas = du.find_elements_by_css_selector('div[class="a-box-group a-spacing-large"]')
    page_upload_canvas = page_upload_canvas[1]
    time.sleep(0.5)

    #Choose file button
    file_input_btn = page_upload_canvas.find_elements_by_css_selector('span[class="a-declarative"]')
    file_input_btn = file_input_btn[1]
    file_input_btn.click()
    
    time.sleep(3)

    pyautogui.typewrite(upload_file)
    pyautogui.press('enter')
    time.sleep(3)
    
    #Upload file button
    file_upload_btn = page_upload_canvas.find_element_by_css_selector('div[class="a-section a-spacing-top-base"]')
    file_upload_btn = file_upload_btn.find_element_by_css_selector('input[name="upload-submit-button"]')

    file_upload_btn.click()
    time.sleep(3)
    
    WebDriverWait(du, 15).until(EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class="a-box a-alert a-alert-success a-spacing-base"]')))
    
    print('Upload Successful')
    time.sleep(3)
    du.quit()


def scroll_down():
    #SCROLL DOWN TO BOTTOM OF THE PAGE#
    time.sleep(0.5)
    
    SCROLL_PAUSE_TIME = 0.5
    
    # Get scroll height
    last_height = du.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to bottom
        du.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = du.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def AZ_login(driver_amz):#with wait for double conf

    try:
        lnk = "https://sellercentral.amazon.com/gp/sign-in/logout.html/ref=xx_logout_dnav_xx"
        driver_amz.get(lnk)
    except:
        pass

    link = (f'https://sellercentral.amazon.com/signin') 
    driver_amz.get(link)
    driver_amz.implicitly_wait(1)
    
    email = 'dean.rusinov@gmail.com'
    password = 'EAsports2020'
    
    css_selector = driver_amz.find_element_by_css_selector
    
    #try to Sing Out?
    try:
        acc_field = WebDriverWait(driver_amz, 5).until(
                EC.presence_of_element_located((By.XPATH , '//*[@id="ap-account-switcher-container"]/div[1]/div/div/div[2]/div[1]/div[1]/div/div/a'))
                )
        #acc_field = css_selector('input[type="email"]')
        acc_field.send_keys(Keys.ENTER)
    
    except:
        pass


    try:
        acc_field = WebDriverWait(driver_amz, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR , 'input[type="email"]'))
                )
        #acc_field = css_selector('input[type="email"]')
        acc_field.send_keys(str(email))
    
    except:
        pass
    acc_field = WebDriverWait(driver_amz, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR , 'input[type="password"]'))
                )
    #acc_field = css_selector('input[type="password"]')
    acc_field.send_keys(str(password))
    
    keep_signed = css_selector('input[name="rememberMe"]')
    keep_signed.click()
    sign_in = css_selector('input[id="signInSubmit"]')
    sign_in.click()
    
    
    try:
        WebDriverWait(driver_amz, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , 'div[id="sc-logo-top"]'))
        )
        #print(element.get_attribute('innerHTML'))
    except:
        print('LogIN in amazon unconfirmed')


#-----------------------------------------------------------------------------#

import pyautogui
import time
import os

from selenium                                import webdriver
from selenium.webdriver.common.by            import By
from selenium.webdriver.support.ui           import WebDriverWait
from selenium.webdriver.support              import expected_conditions as EC
from selenium.webdriver.common.keys          import Keys

if __name__ == "__main__":
    #Amazon upload file location
    upload_file = r'C:\Users\Rusinov\Desktop\Python\upl_inv_to_amz\amazon_inv_file.txt'
    Amazon_Uploader(upload_file)


