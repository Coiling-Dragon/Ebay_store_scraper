# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:43:02 2020

@author: CoilingSnake



https://selenium-python.readthedocs.io/locating-elements.html#locating-elements

elems = driver.find_element_by_xpath("//div[@id='v4-24']")
#elems = elems.get_attribute('innerHTML')
elems = elems.find_elements_by_css_selector("td.details [href]")
links = [elem.get_attribute('href') for elem in elems]

#next_pg = next_pg.find_elements_by_link_text('>')
#text = [elem.text for elem in next_pg]
#print(text)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


"""
def next_scroll_ARG(driver):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(5)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    return False

def next_pageZORO(driver):
    try:
        next_pg = driver.find_element_by_xpath("//div[@class='tppng']")
    except Exception as e:
        print(e)
        return ''
    next_pg = next_pg.find_elements_by_link_text('>')
    links = [elem.get_attribute('href') for elem in next_pg]
    print('Next page link: ')

    if links != []:
        try:
            print(links[0])
            return links[0]
        except Exception as e:
            print(e,'\n link so far is -',links)
            return ''
        
    else:
        print(links,'---------Else statement')
        return ''
        
    
def next_page_items_for_sale(driver):
    try:
        next_pg = driver.find_element_by_xpath("//div[@id='pag-lbl']")
        next_pg = next_pg.find_element_by_xpath("//td[@class='pagn-next']")
        #print(next_pg.get_attribute('innerHTML'))
    except Exception as e:
        print(e)
        return ''
    next_pg = next_pg.find_elements_by_css_selector("td.pagn-next [href]")
    links = [elem.get_attribute('href') for elem in next_pg]
    print('Next page link: ')

    if links != []:
        try:
            print(links[0])
            
            if 'https' not in links[0]:
                return ''
            else:
                return links[0]
            
        except Exception as e:
            print(e,'\n link so far is -',links)
            return ''

    else:
        print(links,'---------Else statement')
        return ''
    

def next_pageURLM123(driver):
    
    next_pg = driver.find_elements_by_css_selector("td.next [href]")
    links = [elem.get_attribute('href') for elem in next_pg]
    print('Next page link: ')
    
    print(links)
    if links != []:
        print(links[0])
        return links[0]
    
    else:
        print(links)
        return ''


def next_pageURL_MF_WW(driver):

            next_pg = driver.find_elements_by_css_selector("a.ebayui-pagination__control")
            
            links = [elem.get_attribute('href') for elem in next_pg]
            print('Next page link: ')
            
            if links != []:
                print(links[1])
                return links[1]
                
            else:
                print(links)
                return '#'


def append_file(output_file,my_list):
    with open(output_file, 'a', encoding='ISO-8859-1') as f:
        for x in my_list:
            f.write(x[0] +','+ x[1] + '\n')
                

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from small_programs.EbayStoreFrontsGetURL import * 
import pandas as pd
from small_programs.EbayIDv1_driver import main_Get_ID_program_driver
from small_programs.EbayIDv2 import main_Get_ID_program

import os





if __name__ == "__main__":
    
    start_time = time.time()
    
    #================================================================= May need to def function_path_finder():
    program_path = os.path.realpath(__file__).split('\\')
    program_path = program_path[0:(len(program_path)-1)]
    program_path = "/".join(program_path)
    if 'Googledrive' in program_path:
        program_path = program_path.split('Googledrive')[0] + 'Googledrive/Python_Shared/In_Out_' + str(os.getenv('username'))
    if 'Google Drive' in program_path:
        program_path = program_path.split('Google Drive')[0] + 'Google Drive/Python_Shared/In_Out_' + str(os.getenv('username'))
    print(program_path)
    #=================================================================
    
    file_folder = program_path + '/files_Storefront_scraper/'
    
    #file_folder = 'files_Storefront_scraper/'
    
    input_file = file_folder + 'StoreFront input.csv'
    output_file = file_folder + 'inputURL.csv'
    
    with open(output_file, 'w', encoding='ISO-8859-1') as f:
        f.write('URL,Store\n')
    
    sys_username = str(os.getenv('username'))
    options = webdriver.ChromeOptions()
    # TELL WHERE IS THE DATA DIR
    options.add_argument(r"--user-data-dir=C:\Users\{0}\AppData\Local\Google\Chrome\User Data\Profile {0}".format(
        sys_username))
    # USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
    options.add_argument('--profile-directory=Profile {0}'.format(sys_username))
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver.implicitly_wait(1)
    
    with open(input_file, 'r', encoding='ISO-8859-1') as f:
        lines = f.readlines()
        data = [row.strip() for row in lines]#foramts the data in to table
        
    #header = data[0:1][0]#slice the first row that is header
    list_of_links = data[1:]
    
    scroll_pg = False
    for store_link in list_of_links:#loop trough the stores
        
        uk_store_switch = False
        next_pg = store_link.split(',')[0]#next_pg is a string
        
        if 'MF' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = MF_storefront(driver,next_pg)
                next_pg = next_pageURL_MF_WW(driver)
                append_file(output_file,links)
                if next_pg[-1] == '#':
                    next_pg = ''
            
        if 'WW' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = WW_storefront(driver,next_pg)
                next_pg = next_pageURL_MF_WW(driver)
                append_file(output_file,links)
                if next_pg[-1] == '#':
                    next_pg = ''

        if 'VIP' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = VIP(driver,next_pg)
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
            
        if 'M123' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = M123(driver,next_pg)
                next_pg = next_pageURLM123(driver)
                append_file(output_file,links)
                
        if 'SW' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = SW(driver,next_pg)
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
                
        if 'PBA' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = PBA(driver,next_pg)
                next_pg = next_pageURLM123(driver)
                append_file(output_file,links)
                
        if 'PAS' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = PAS(driver,next_pg)
                next_pg = next_pageURLM123(driver)
                append_file(output_file,links)
                
        if 'MSL' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = MSL(driver,next_pg)
                next_pg = next_pageURLM123(driver)
                append_file(output_file,links)
                
        if 'PC' in store_link:# NOT done
            
            while next_pg != '':
                if next_pg is None:
                    break
                links = PC(driver,next_pg)
                next_pg = next_pageURLM123(driver)
                append_file(output_file,links)
                
        if 'ZOR' in store_link:# NOT done
            
            while next_pg != '':
                if next_pg is None:
                    break

                links = ZORO(driver,next_pg)
                next_pg = next_pageZORO(driver)
                append_file(output_file,links)
                
                
        if 'SAM' in store_link:
            
            while next_pg != '':
                if next_pg is None:
                    break
                
                links = SAM(driver,next_pg)
                next_pg = next_pageURLM123(driver)
                append_file(output_file,links)
                
                
        if 'ARG' in store_link:
            scroll_pg = True
            uk_store_switch = True
            while next_pg != '':
                if next_pg is None:
                    break
                if scroll_pg is False:
                    break
                
                ARG(driver,next_pg)
                scroll_pg = next_scroll_ARG(driver)
                links = ARG(driver,'')
                append_file(output_file,links)
    
    
        if 'FORZ' in store_link:
            while next_pg != '':
                if next_pg is None:
                    break
                
                links = items_for_sale(driver,next_pg,'FORZ')
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
                
                
        if 'CPO' in store_link:
            while next_pg != '':
                if next_pg is None:
                    break
                
                links = items_for_sale(driver,next_pg,'CPO')
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
                
                
        if 'ABN' in store_link:
            while next_pg != '':
                if next_pg is None:
                    break
                
                links = items_for_sale(driver,next_pg,'ABN')
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
                
        if 'PNM' in store_link:
            while next_pg != '':
                if next_pg is None:
                    break
                
                links = items_for_sale(driver,next_pg,'PNM')
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
                
                
        if 'items' in store_link:
            while next_pg != '':
                if next_pg is None:
                    break
                
                links = items_for_sale(driver,next_pg,'items')
                next_pg = next_page_items_for_sale(driver)
                append_file(output_file,links)
                
    '''use main_Get_ID_program_driver if there were UK stores'''
    if uk_store_switch == True:
        
        main_Get_ID_program_driver(driver,file_folder)
        driver.close()
        
    else:
        driver.close()
        main_Get_ID_program(file_folder)
    
    elapsed_time = round((time.time() - start_time),2)
    
    hours_ = elapsed_time//3600
    min_ = (elapsed_time%3600)//60
    sec_ = (elapsed_time%60)
    
    
    print("\n\nFinished in:",int(hours_),'Hours,',int(min_),'min,',(sec_),'sec.')

    time_str = str(time.strftime('%Y-%m-%d %Hh%Ms', time.localtime(time.time()) ))
    print(time_str)
    
 #'''