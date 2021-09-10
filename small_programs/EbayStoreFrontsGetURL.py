'''
https://selenium-python.readthedocs.io/locating-elements.html#locating-elements

elems = driver.find_element_by_xpath("//div[@id='v4-24']")
#elems = elems.get_attribute('innerHTML')
elems = elems.find_elements_by_css_selector("td.details [href]")
links = [elem.get_attribute('href') for elem in elems]


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
'''
def MF_storefront(driver,website):

    driver.get(website)
    elems = driver.find_elements_by_css_selector("div.s-item__image-section [href]")
    links = [(elem.get_attribute('href'),'MF') for elem in elems]
    return links

def WW_storefront(driver,website):

    driver.get(website)
    elems = driver.find_elements_by_css_selector("div.s-item__image-section [href]")
    links = [(elem.get_attribute('href'),'WW') for elem in elems]
    return links

def VIP_storefront(driver,website):

    driver.get(website)
    elems = driver.find_elements_by_css_selector("div.s-item__image-section [href]")
    links = [(elem.get_attribute('href'),'VIP') for elem in elems]
    return links


def ARG(driver,Argus):
    website = Argus
    
    if website != '':
        driver.get(website)
        
    elems = driver.find_element_by_xpath("//div[@id='results']")
    #print(elems.get_attribute('innerHTML'))
    elems = elems.find_elements_by_xpath("//a[@class='resultItemLink']")
    links = [(elem.get_attribute('href'),'ARG') for elem in elems]
    return links


def SW(driver,Sweeteater):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Sweeteater
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'SW') for elem in elems]
    return links


def MF(driver,Music_friend):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Music_friend
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("h3.lvtitle [href]")
    links = [(elem.get_attribute('href'),'MF') for elem in elems]
    return links


def WW(driver,Woodwind):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Woodwind
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("h3.lvtitle [href]")
    links = [(elem.get_attribute('href'),'WW') for elem in elems]
    return links


def VIP(driver,vip_outlet):
    '''
    items for sale
    
    '''
    
    website = vip_outlet
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("h3.lvtitle [href]")
    links = [(elem.get_attribute('href'),'VIP') for elem in elems]
    return links


def items_for_sale(driver,website,store):
    '''
    items for sale
    '''
    driver.get(website)
    elems = driver.find_elements_by_css_selector("h3.lvtitle [href]")
    links = [(elem.get_attribute('href'),store) for elem in elems]
    return links



def M123(driver,Music_123):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Music_123
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'M123') for elem in elems]
    return links


def PBA(driver,Pitbull_audio):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Pitbull_audio
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'PBA') for elem in elems]
    return links


def PAS(driver,proaudiostar):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = proaudiostar
    
    driver.get(website)
    elems = driver.find_element_by_xpath("//td[@class='r3_c']")
    #elems = elems.get_attribute('innerHTML')
    elems = elems.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'PAS') for elem in elems]
    return links


def MSL(driver,MusicStoreLive):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = MusicStoreLive
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'MSL') for elem in elems]
    return links


def PC(driver,Perfect):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Perfect
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'PC') for elem in elems]
    return links


def ZORO(driver,Zoro):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    
    website = Zoro
    
    driver.get(website)
    elems = driver.find_elements_by_css_selector("div.title [href]")
    links = [(elem.get_attribute('href'),'ZOR') for elem in elems]
    return links


def SAM(driver,sam_ash):
    '''
    function needs:
    
    imports:
    from selenium import webdriver
    
    code:
    driver = webdriver.Chrome('chromedriver.exe')
    store_name = (store_name(search_word))
    driver.close()
    
    '''
    website = sam_ash
    driver.get(website)
    elems = driver.find_elements_by_css_selector("td.details [href]")
    links = [(elem.get_attribute('href'),'SAM') for elem in elems]
    return links


from selenium import webdriver
import time


if __name__ == "__main__":
    
    from EbayIDv2 import main_Get_ID_program as id_scrape
    
    start_time = time.time()
    
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(1)
    
    with open("inputURL.csv", 'w', encoding="ISO-8859-1") as f:
        f.write('URL,Store\n')

    
    with open("EbayStoreFronts_UPC_to_URL.csv", 'r', encoding="ISO-8859-1") as f:
        lines = f.readlines()
        data = [(row.strip()).split(',') for row in lines]#foramts the data in to table
        
            
    #header = data[0:1][0]#slice the first row that is header
    data = data[1:]
    #print(data)
    #print(header)
    c=1
    
    for row in data:#loop trough the rows in the input mapper file
    
        specific_store_upc = row[0].split(':::')
        links = []
        
        for store_upc in specific_store_upc:#loop trough the stores
            #print('\n'+store_upc, upc, id_row)
            
            if 'GC' in store_upc:
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
                                
            if 'MF' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Music_friend = ('https://www.ebay.com/sch/m.html?_ssn=musiciansfriend&_from=R40&_sacat=0&_nkw='
                                +search_word
                                +'&_sop=16&_clu=2&_fcid=1&_localstpos=83001&_stpos=83001&gbr=1&_zpclkd=1')
                links = links + MF(driver,Music_friend)
                
                
            if 'M123' in store_upc:
                search_word = store_upc.split('?')[1]
                if search_word == '':
                    continue
                Music_123 = ('http://www.ebaystores.com/Music123/_i.html?_nkw='
                             +search_word
                             +'&submit=Search&_sop=3&_sacat=Music123&_sid=4598174&_sc=1')
                links = links + M123(driver,Music_123)
                
            if 'WW' in store_upc:
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
        
        print('Row:',c)
        c+=1
    
        with open("inputURL.csv", 'a', encoding="ISO-8859-1") as f:
            for url_store in links:
                f.write(url_store[0]+','+url_store[1]+'\n')
                
    driver.close()
    
    file_folder = ''
    id_scrape(file_folder)

    elapsed_time = round((time.time() - start_time),2)
    print("\n\nFinished in: ",elapsed_time,'sec')
#'''