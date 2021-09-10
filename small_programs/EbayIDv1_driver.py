# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:27:04 2019

#Ebay crawler main program

@author: CoilingDragon

----------------some intresting searches for Beautiful Soup:
import re
soup.find_all(class_=re.compile("itl"))
# [<p class="title"><b>The Dormouse's story</b></p>]

css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]

soup.find('p', attrs={'class':'body strikeout'}).text
# [<p class="body strikeout"></p>]

soup.head.title
# <title>The Dormouse's story</title>
-or-
soup.find("head").find("title")
# <title>The Dormouse's story</title>

"""



#------------------------------FUNCTIONS--------------------------------------#
def get_random_line_from_txtfile(txtfile_name):
    '''rl = get_random_line_from_txtfile(txtfile_name): - Function to get random linse in txt file. Uses numpy'''
    random_line = ''

    try:
        with open(txtfile_name, 'r', encoding='ISO-8859-1') as f:
            lines = f.readlines()

        if len(lines) > 0:
            prng = np.random.RandomState()
            #prng is <mtrand.RandomState object>
            index = prng.permutation(len(lines) - 1)
            #indx is a randomised array/list of the rows in the file
            idx = np.asarray(index, dtype=np.integer)[0]
            #idx returns the 0 indexed row of the array/list
            random_line = lines[int(idx)]
            random_line = random_line.replace("\n", "")

    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))

    finally:
        return random_line


def get_the_price(soup):
    try:
        varHTML = soup.find('div', attrs={'class':'u-flL w29 vi-price'}).text
        varHTML = str(varHTML).replace(',','')
        output = (re.findall("\d+.\d+", varHTML)[0])
        #output = str(varHTML).split('$')[1].split('\n')[0]

    except:# Exception as ex:
        output = "get_the_price() exception. (is it a bug)"
        #print(output,str(ex))

    finally:
        return output
    

def get_the_shipping(soup):
    try:
        varHTML = soup.find('span', attrs={'id':'fshippingCost'}).text
        varHTML = str(varHTML).replace(',','')
        output = (re.findall("\d+.\d+", str(varHTML))[0])
        #output = str(varHTML).split('$')[1].split('\n')[0]

    except:# Exception as ex:
        output = "get_the_price() exception. (is it a bug)"
        #print(output,str(ex))

    finally:
        return output


def get_the_condition(soup):
    try:
        varHTML = soup.find('div', attrs={'class':'u-flL condText'}).text
        output = varHTML

    except:# Exception as ex:
        output = "get_the_condition() exception. (is it a bug)"
        #print(output,str(ex))

    finally:
        return output

def item_spec_table_split(soup,class_name,split_at,elem_arr_idx):
    '''Gets the item specification table content and splits it at spliter, returns result'''
    try:
        varHTML = soup.find(class_=class_name).get_text()
        output = str(varHTML).split(split_at)[1].split('\n')[elem_arr_idx]
        output = output.strip()
        #output = re.sub(r'[^0-9a-zA-Z .-]' , '' , output)

    except:# Exception as ex:
        output = "No "+ split_at +" (is it a bug)."
        #print(output,str(ex))

    finally:
        return output
    
    
def item_spec_table_split_TOUPPER(soup,class_name,split_at,elem_arr_idx):#.upper()
    '''Gets the item specification table content and splits it at spliter, returns result'''
    try:
        varHTML = soup.find(class_=class_name).get_text().upper()
        split_at = split_at.upper()
        output = str(varHTML).split(split_at)[1].split('\n')[elem_arr_idx]
        output = output.strip()
        #output = re.sub(r'[^0-9a-zA-Z .-]' , '' , output)

    except:# Exception as ex:
        output = "No "+ split_at +" (is it a bug)."
        #print(output,str(ex))

    finally:
        return output
    

def get_category(soup):
    try:
        category_list = soup.find_all("li", attrs={'itemprop':'itemListElement'})
    
        category = []
        for each in category_list:
            category = category + [each.text,]
        category = ','.join(category)
    except:
        category = ''
    finally:
        return category


def scraper_program_loop_driver(driver,input_file_name,end_file_name):

    global error_handler
    global soup
    global item_str
    
    item_str = 'Exception in scraper_program_loop_driver()'

    c = 0 #counter for the items scraped
    
    try:
        with open(end_file_name, "r", encoding='ISO-8859-1') as write_file:
            lines_check = write_file.readlines()
            scraped_items = len(lines_check)-1
            #print(lines_check)
            del lines_check

            
        with open(input_file_name, 'r', encoding='ISO-8859-1') as f:
            lines = f.readlines()
            
            if len(lines) > 0:
                for L in lines:

                    if c == 0 or c <= scraped_items: # skip scraped rows
                        c +=1
                        continue

                    if L == "": #skip empty rows
                        c +=1
                        continue
                    
                    url = L.split(',')[0]
                    store = L.split(',')[1].strip()
                    
                    driver.get(url)
                    
                    try:
                        dr_response = WebDriverWait(driver, 6).until(
                        EC.presence_of_element_located((By.XPATH , '//body')))
                        dr_response = dr_response.get_attribute('innerHTML')
                        response = 200
                    except:
                        response = 1
                    
                    
                    if response == 200:
                        
                        print('\n\nSuccess!(webdriver)\n')
                        soup = BeautifulSoup(dr_response, 'html.parser') 

                        
                        category = get_category(soup).lower()
                        
                        if 'clothing' in category or 'shoes' in category or 'books' in category or 'dvd' in category or 'records' in category:
                            if 'netbooks' in category:
                                print(category.replace('\n',''))
                            else:
                                print('\nCategory contains unwanted items: ')
                                print(category.replace('\n',''))
                                print('SKIPPING THIS ITEM')
                                continue
                        
                        cond = get_the_condition(soup).replace(',','')
                        print(cond)
                        if cond.lower() == 'new' or cond.lower() == 'brand new':
                            print('ITEM - condition  NEW')
                            
                        elif "VIP" in store and (cond.lower() == 'seller refurbished' or cond.lower() == 'new' or cond.lower() == 'brand new'):
                            print(f'ITEM from VIP -{cond}')
                            
                        else:
                            print('SKIPPING THIS ITEM - condition not NEW')
                            continue
                        

                        #setings for item spec. table scrape
                        class_name = 'itemAttr'
                        elem_arr_idx = 2
                        
                        split_at = 'UPC:'
                        upc = item_spec_table_split(soup,class_name,split_at,elem_arr_idx)
                        
                        
                        if '(is it a bug)' in upc:
                            upc = item_spec_table_split_TOUPPER(soup,class_name,split_at,elem_arr_idx)
                        
                        
                        split_at = 'EAN:'
                        ean = item_spec_table_split(soup,class_name,split_at,elem_arr_idx)
                        #print(ean)
                        if '(is it a bug)' in ean:
                            ean = item_spec_table_split_TOUPPER(soup,class_name,split_at,elem_arr_idx)
        
        
                        if upc == 'Doesnotapply' or '(is it a bug)' in upc:
                            upc = ean
                        upc = store + "?" + upc
                        
                        print(upc)
        
                        
                        split_at = 'MPN:'
                        mpn = item_spec_table_split(soup,class_name,split_at,elem_arr_idx)
                        mpn = mpn.replace(',', '&').replace('"','').replace("'","")
                        if '(is it a bug)' in mpn:
                            mpn = item_spec_table_split_TOUPPER(soup,class_name,split_at,elem_arr_idx)
                        
                        
                        split_at = 'Brand:'
                        brand = item_spec_table_split(soup,class_name,split_at,elem_arr_idx)
                        brand = brand.replace(',', '&').replace('"','').replace("'","")
                        if '(is it a bug)' in brand:
                            brand = item_spec_table_split_TOUPPER(soup,class_name,split_at,elem_arr_idx)
                            

                        #price scrape
                        price = get_the_price(soup)
                        print(price,':price')
                        

                        shipping = get_the_shipping(soup)
                        print(shipping,':shipping')

                        
                        brand = store + '?' + brand + '?' + mpn
                        
                        try:
                            price_ship_sum = round(float(shipping) + float(price),2)
                        except:# Exception as ex:
                            price_ship_sum = price
                            #print(ex)
                        
                        price_ship_sum = str(price_ship_sum)

                    elif response != 200:
                        print('Not Found.', response.status_code)
                        upc , price_ship_sum , brand , cond  = 'response != 200:','no response','no response','no response','no response'


                    item_str = upc +"," + brand + "," + price_ship_sum + "," + cond + "," + url + '\n'
                    #print('\n\n'+item_str)
                    try:
                        with open(end_file_name, "a", encoding='ISO-8859-1') as write_file:
                            write_file.write(item_str)
                    except:
                        with open(end_file_name, "a", encoding='utf-8') as write_file:
                            write_file.write(re.sub(r'[^\x00-\x7f]',r'',item_str))
                    
                    print(f'Currently just scraped row {c}')
                    c +=1

        error_handler = False

    except Exception as ex:
        print(f'Exception in scraper, currently on row {c}')
        print(str(ex))

        with open('Error.csv', "a", encoding='utf-8') as write_file:
            write_file.write(item_str)
            print(f'ERROR>> {ex} <<Currently on {url} and row {c}\n')


def main_Get_ID_program_driver(driver,file_folder):
    '''
    imports:
    import numpy as np
    import requests
    import time
    from bs4 import BeautifulSoup
    
    Ebay ID scraper:
        in files - inputURL.csv
        out files - ID outs.csv, Error.csv
        
        gets the INFO from URLs in inputURL.csv and writes it in ID outs.csv
        Errors are writen in Error.csv
    '''


    global error_handler
    global soup
    global item_str
    #print("Get IDs is set to ---"+file_folder)
    
    input_file_name = file_folder+"inputURL.csv"
    end_file_name = file_folder+"ID outs.csv"
    #print(end_file_name)
    
    with open(end_file_name, "w", encoding='ISO-8859-1') as write_file:
        write_file.write("UPC,Store,price_ship_sum,cond,URL\n")

    error_handler = True
    
    while error_handler == True:
        scraper_program_loop_driver(driver,input_file_name,end_file_name)
        
    data_frame = pd.read_csv(end_file_name , engine='python').drop_duplicates(subset='UPC', keep='first', inplace=False)
    data_frame.to_csv(file_folder+'ID outs_nonDuplicate.csv', index=False , encoding = 'utf-8')

#------------------------------FUNCTIONS--------------------------------------#

import numpy as np
import requests
import time
from bs4 import BeautifulSoup
#from csv import writer
import pandas as pd
import re


from selenium                                import webdriver
from selenium.webdriver.common.by            import By
from selenium.webdriver.support.ui           import WebDriverWait
from selenium.webdriver.support              import expected_conditions as EC



if __name__ == "__main__":
    #print('__name__ == "__main__":')
    
    start_time = time.time()
    
    file_folder = ''
    
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(1)
    main_Get_ID_program_driver(driver,file_folder)
    
    elapsed_time = round((time.time() - start_time),2)
    print("\n\nFinished in: ",elapsed_time,'sec')