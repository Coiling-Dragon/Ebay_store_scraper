
"""
# =============================================================================
# 
# By CoilingDragon
# 
# =============================================================================
"""

def sort_Price_datatable(store_upc,Row,ASIN,SKU,UPC,Store,SaleChan,Status,old_price,file_folder):
    
    #'Row','ASIN','SKU','UPC','Store','SaleChan','Status','URL','old_price'>>'new_price'
    # URL,new_price from "ID outs.csv"
    oos_price = '9999999'
    oos_URL = ''
    if old_price == '':
        old_price = 0
    
    data_frame = pd.read_csv(file_folder+"ID outs.csv", encoding="ISO-8859-1")
    data_frame = data_frame.sort_values(by=['price_ship_sum'])
    
    
    brand_confirmation = Store #add the brands hire
    
    
    rows = (data_frame.values)
    
    if len(rows) == 0:
        print('Item is OOS')
        #append to file New_Prices.csv as OOS
        with open(out_newPrices_file, "a", encoding="ISO-8859-1") as write_file:
            write_file.write(','.join([Row,ASIN,SKU,UPC,Store,SaleChan,Status,
                                       oos_URL,str(oos_price) +'\n']))
        
    else:
        c=0
        for row in rows:# ROWS IN ID OUTS.csv
            #row[1] brand
            new_price = row[2]
            new_url = row[4]
            
            print (f'\n-----Checking Brankd/MPN\n',row[1].lower(),'in',brand_confirmation.lower(),'\n-----Condition: ',row[3].lower())
            
            if str(row[1].lower()).strip() in str(brand_confirmation.lower()).strip():# and (row[3].lower() == 'new' or row[3].lower() == 'brand new'): #confirm the condition, brand and MPN
                #price manipulation 'old_price*0.7'>'new_price':: if old_pr > new_pr ::: float(x)
                print (f'\nItem found: row {c}')
                
                try:
                    print(f'old price: {old_price} , new price: {new_price}')
                    if float(old_price)*0.7 > float(new_price) and old_price != oos_price :
                        new_price = old_price
                except:
                    new_price = oos_price
                    print('exception happened when converting price to floats')
                
                #append to file New_Prices.csv as INSTOCK
                with open(out_newPrices_file, "a", encoding="ISO-8859-1") as write_file:
                    write_file.write(','.join([Row,ASIN,SKU,UPC,Store,SaleChan,
                                               Status,new_url,str(new_price) +'\n']))
                break
            else:
                print (f'\nWRONG NPN/BRAND: row {c}')
                #append to file 'Potential_Wrong_items.csv'. This condition is executed for all rols until the a correct one is reached
                with open(potential_wrongItems_file, "a", encoding="ISO-8859-1") as write_file:
                     write_file.write(','.join([Row,ASIN,SKU,store_upc,row[1],SaleChan,
                                                Status,new_url,'Brand or condition not confirmed' +'\n']))
                
                c+=1
                if c == len(rows):# sets the condition c = len(of csv) so we dont duplikate final results
                    
                    #append to file New_Prices.csv as OOS
                    with open(out_newPrices_file, "a", encoding="ISO-8859-1") as write_file:
                        write_file.write(','.join([Row,ASIN,SKU,UPC,Store,SaleChan,
                                                   Status,row[1],str(oos_price) +'\n']))


def error_handleloop(file_folder):
    global error_occured
    global potential_wrongItems_file
    global input_mapper_file
    global out_newPrices_file
    
    
    
    with open(out_newPrices_file, "r", encoding="ISO-8859-1") as write_file:
        lines_check = write_file.readlines()
        scraped_items = len(lines_check)-1
        #print(lines_check)
        lines_check = []
    
    with open(input_mapper_file, 'r', encoding="ISO-8859-1") as f:
        lines = f.readlines()
        data = [(row.strip()).split(',') for row in lines]#foramts the data in to table
        
    #header = data[0:1][0]#slice the first row that is header
    data = data[1:]
    #print(header)
    
    c = 1 #counter for the items scraped
    for row in data:#loop trough the rows in the input mapper file
        #print(row)
        if c <= scraped_items: # skip scraped rows
            c +=1
            continue
    
        specific_store_upc = row[3].split(':::')
        links = []
        
        for store_upc in specific_store_upc:#loop trough the stores
            #print('\n'+store_upc, upc, id_row)
            
            if 'GC_' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Music_friend = ('https://www.ebay.com/sch/m.html?_ssn=musiciansfriend&_from=R40&_sacat=0&_nkw='
                                +search_word
                                +'&_sop=16&_clu=2&_fcid=1&_localstpos=83001&_stpos=83001&gbr=1&_zpclkd=1')
                Woodwind = ('https://www.ebay.com/sch/m.html?_ssn=woodwindbrasswind&_from=R40&_sacat=0&_nkw='
                            +search_word
                            +'&_sop=16&_clu=2&_fcid=1&_localstpos=83001&_stpos=83001&gbr=1&_zpclkd=1')
                Music_123 = ('http://www.ebaystores.com/Music123/_i.html?_nkw='
                             +search_word
                             +'&submit=Search&_sop=3&_sacat=Music123&_sid=4598174&_sc=1')
                links = links + MF(driver,Music_friend)
                links = links + WW(driver,Woodwind)
                links = links + M123(driver,Music_123)
                
            if 'MF_' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Music_friend = ('https://www.ebay.com/sch/m.html?_ssn=musiciansfriend&_from=R40&_sacat=0&_nkw='
                                +search_word
                                +'&_sop=16&_clu=2&_fcid=1&_localstpos=83001&_stpos=83001&gbr=1&_zpclkd=1')
                links = links + MF(driver,Music_friend)
                
                
            if 'M123_' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Music_123 = ('http://www.ebaystores.com/Music123/_i.html?_nkw='
                             +search_word
                             +'&submit=Search&_sop=3&_sacat=Music123&_sid=4598174&_sc=1')
                links = links + M123(driver,Music_123)
                
            if 'WW_' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Woodwind = ('https://www.ebay.com/sch/m.html?_ssn=woodwindbrasswind&_from=R40&_sacat=0&_nkw='
                            +search_word
                            +'&_sop=16&_clu=2&_fcid=1&_localstpos=83001&_stpos=83001&gbr=1&_zpclkd=1')
                links = links + WW(driver,Woodwind) 
                
            if 'SW' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Sweeteater = ('http://www.ebaystores.com/Sweetwater-Sound/_i.html?rt=nc&_nkw='
                              +search_word
                              +'&_sid=36121123&_sticky=1&_trksid=p4634.c0.m14&_sop=16&_sc=1')
                links = links + SW(driver,Sweeteater)
                
            if 'PBA' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Pitbull_audio = ('http://www.ebaystores.com/PitbullAudioandDVD/_i.html?_nkw='
                                 +search_word
                                 +'&submit=Search&_sacat=PitbullAudioandDVD&_sid=22210677')
                links = links + PBA(driver,Pitbull_audio)
                
            if 'PAS' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                proaudiostar = ('http://www.ebaystores.com/proaudiostar/_i.html?rt=nc&_nkw='
                                +search_word
                                +'&_sacat=proaudiostar&_sc=1&_sid=336450849&_sticky=1&_trksid=p4634.c0.m14&_sop=16&_sc=1')
                links = links + PAS(driver,proaudiostar)
                
            if 'MSL' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                MusicStoreLive = ('http://www.ebaystores.com/MusicStoreLive/_i.html?rt=nc&_nkw='
                                  +search_word
                                  +'&_sacat=MusicStoreLive&_sc=1&_sid=105115575&_sticky=1&_trksid=p4634.c0.m14&_sop=16&_sc=1')
                links = links + MSL(driver,MusicStoreLive)
    
            if 'PC' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Perfect = ('http://www.ebaystores.com/Perfect-Circuit-Audio/_i.html?rt=nc&_nkw='
                           +search_word
                           +'&_sc=1&_sid=38959239&_sticky=1&_trksid=p4634.c0.m14&_sop=16&_sc=1')
                links = links + PC(driver,Perfect)
    
            if 'ZOR' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Zoro = ('http://www.ebaystores.com/Zoro-Tools/_i.html?rt=nc&_nkw='
                        +search_word
                        +'&_sc=1&_sid=1113381714&_sticky=1&_trksid=p4634.m14&_sop=16&_sc=1')
                links = links + ZORO(driver,Zoro)
    
            if 'SAM' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                sam_ash = ('http://www.ebaystores.com/Sam-Ash-Music-Direct/_i.html?rt=nc&_nkw='
                                 +search_word
                                 +'&_sid=1111655870&_sticky=1&_trksid=p4634.c0.m14&_sop=2&_sc=1')
                links = links + SAM(driver,sam_ash)
                
            if 'VIP' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                vip_outlet = ('https://www.ebay.com/sch/m.html?_ssn=vipoutlet&_from=R40&_sacat=0&_nkw='
                                 +search_word
                                 +'&_sop=15')
                links = links + VIP(driver,vip_outlet)
            
            if 'ARG' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                arg_items_store = ('http://www.ebaystores.co.uk/argos?keywords='
                                 +search_word
                                 +'&aspectFilter=%7B%7D&sortOrder=BestMatch')
                links = links + ARG(driver,arg_items_store)
                
            if 'FORZ' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                website = ('https://www.ebay.com/sch/m.html?_odkw=&_ssn=forzasports&_armrs=1&_nkw='
                                 +search_word
                                 +'&_sacat=0')
                links = links + items_for_sale(driver,website,'FORZ')
                
            if 'CPO' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                website = ('https://www.ebay.com/sch/m.html?_odkw=&_ssn=cpo-outlets&_armrs=1&_osacat=0&_from=R40&_trksid=m570.l1313&_nkw='
                                 +search_word
                                 +'&_sacat=0')
                links = links + items_for_sale(driver,website,'CPO')
                
                                
            if 'ABN' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                website = ('https://www.ebay.com/sch/m.html?_odkw=&_ssn=autobodynow&_armrs=1&_osacat=0&_from=R40&_trksid=m570.l1313&_nkw='
                                 +search_word
                                 +'&_sacat=0')
                links = links + items_for_sale(driver,website,'ABN')
                
                
            if 'PNM' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                website = ('https://www.ebay.com/sch/m.html?_odkw=&_ssn=pens_n_more&_osacat=0&_from=R40&_trksid=m570.l1313&_nkw='
                                 +search_word
                                 +'&_sacat=0')
                links = links + items_for_sale(driver,website,'PNM')
    
        #print(links) links are returned as a list of tuples [(href,store),()...]
        #link_fix = [(url_store[0]+','+url_store[1]+'\n') for url_store in links]
    
        #print(links)
        with open(file_folder+"inputURL.csv", 'w', encoding="ISO-8859-1") as f:
            f.write('URL,Store\n')
            for url_store in links:
                f.write(url_store[0]+','+url_store[1]+'\n')
               
        #-----invoke EbayID 1 or 2
        uk_stores = ['ARG',]
        uk_switch = False
        
        #switch between EbayID 1 or 2 depending on info in UPC col
        for uk_store in uk_stores:
            
            if uk_store in row[3]:
                uk_switch = True

        if uk_switch == True:
            main_Get_ID_program_driver(driver,file_folder)

        else:
            main_Get_ID_program(file_folder)
        
        
        
        id_row = row[0]
        asin = row[1]
        sku = row[2]
        upc = row[3]
        store = row[4]#compare old brand, MPN with the new
        salechan = row[5]
        status = row[6]
        url_old = row[7]
        old_price = row[8]#compare old Price with the new
        
        sort_Price_datatable(store_upc,id_row,asin,sku,upc,store,salechan,status,old_price,file_folder)
        c +=1
    
    error_occured = False


def main_mapper_program(file_folder):
    
    global error_occured
    global potential_wrongItems_file
    global input_mapper_file
    global out_newPrices_file
    global driver
    import psutil #for killing processes
    
    file_folder = file_folder
    print("this is where Mapper is set to----"+file_folder)
    out_newPrices_file = file_folder + 'New Prices.csv'
    input_mapper_file = file_folder + 'inputMapper.csv'
    out_newPrices_file = file_folder + 'New Prices.csv'
    potential_wrongItems_file = file_folder + 'Potential Wrong items.csv'
    
    with open(out_newPrices_file, "w", encoding="ISO-8859-1") as write_file:
        write_file.write(','.join(['Row','ASIN','SKU','UPC','Store','SaleChan','Status','URL','Price'+'\n']))
    
    with open(potential_wrongItems_file, "w", encoding="ISO-8859-1") as write_file:
        write_file.write(','.join(['Row','ASIN','SKU','UPC','Store','SaleChan','Status','URL','Reason'+'\n']))
    
    error_occured = True
    while error_occured == True:
        
        try:
            sys_username = str(os.getenv('username'))
            options = webdriver.ChromeOptions()
            # TELL WHERE IS THE DATA DIR
            options.add_argument(r"--user-data-dir=C:\Users\{0}\AppData\Local\Google\Chrome\User Data\Profile {0}".format(
                sys_username))
            # USE THIS IF YOU NEED TO HAVE MULTIPLE PROFILES
            options.add_argument('--profile-directory=Profile {0}'.format(sys_username))
            driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
            
            driver.implicitly_wait(1)
            error_handleloop(file_folder)
            
        except Exception as ex:
            print(ex,'Error in main_mapper_program()')
            #raise ex
            try:
                for proc in psutil.process_iter():
                    #print(proc.name())
                    if 'chrome' in proc.name():
                        proc.kill()
            except:
                pass
            
    driver.close()
    new_price_data_frame = pd.read_csv(out_newPrices_file, encoding="ISO-8859-1")
    new_price_data_frame.to_csv(input_mapper_file, index=False, encoding="ISO-8859-1")
    file_prep(new_price_data_frame,file_folder)


import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from small_programs.EbayIDv2 import main_Get_ID_program
from small_programs.EbayIDv1_driver import main_Get_ID_program_driver
from small_programs.EbayStoreFrontsGetURL import *
from small_programs.UploadFilePrep import *
import pandas as pd
import numpy as np
import os

if __name__ == "__main__":

    start_time = time.time()
    
    #user_name = os.path.expanduser("~").split('\\')[2]
    user_name = str(os.getenv('username'))
    print(user_name+'---------------\n')
    
    
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
    
    file_folder = program_path + '/files_Mapper/'
    
    
    #file_folder = 'files_Mapper/'
    
    main_mapper_program(file_folder)
    
    
    elapsed_time = round((time.time() - start_time),2)
    
    hours_ = elapsed_time//3600
    min_ = (elapsed_time%3600)//60
    sec_ = (elapsed_time%60)
    
    
    print("\n\nFinished in:",int(hours_),'Hours,',int(min_),'min,',(sec_),'sec.')

    time_str = str(time.strftime('%Y-%m-%d %Hh%Ms', time.localtime(time.time()) ))
    print(time_str)