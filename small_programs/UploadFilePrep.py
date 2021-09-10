'''
This is upload file preperation for Amazon update and Bqool repriceing

'''


def handling_time_store_check(upc,handling_time):
    if 'PNM' in upc:
        return str(int(handling_time)+4)+'\n'
    else:
        return str(handling_time)+'\n'
    

def amazon_inv_file(new_price_data_frame,out_folder):
    '''sku	price	minimum-seller-allowed-price	maximum-seller-allowed-price	quantity	handling-time	fulfillment-channel'''
    data = new_price_data_frame.values
    '''Row[0]	ASIN[1]	SKU[2]	UPC[3]	Store[4]	SaleChan[5]	Status[6]	URL[7]	Price[8]'''#data COLLS
    cell = []
    rows = []
    handling_time = '2'
    quantity = '2'
    
    with open(out_folder+'amazon_inv_file.txt','w',encoding = "ISO-8859-1") as f:
        f.write('\t'.join(['sku','price','minimum-seller-allowed-price','maximum-seller-allowed-price','quantity','handling-time\n']))
        for each in data:

            cell = ['cell[0]','cell[1]','cell[2]','cell[3]','cell[4]','cell[5]']
            cell[0] = str(each[2]) #sku
            
            #cell[1]#price
            if each[8] != 9999999:
                cell[1] = str(round((each[8]*1.40),2))
                cell[4] = quantity #cell[4] is quantity
            
            else:
                cell[1] = '' #price is each[8] and is int
                cell[4] = '0' #cell[4] is quantity
                
            #print(each[6])
            if each[6] != 'active':
                cell[4] = '0'
            if each[6] == 'actNoRep' and each[8] != 9999999:#check status!
                cell[4] = quantity 
                  
            cell[2] = ''#minimum-seller-allowed-price
            cell[3] = ''#maximum-seller-allowed-price
            #cell[4] is quantity
            
            '''handling_time store check'''
            cell[5] = handling_time_store_check(each[3],handling_time)
            #cell[6] = '\n'#fulfillment-channel OUTDATED
            rows = rows + ['\t'.join(cell)]
        f.writelines(rows)


def bqool_inv_file(new_price_data_frame,out_folder):
    '''Channel	SellerSKU	Cost	Rule Name	Min Price	Max Price	Shipping	add-delete	Group	Enable Repricing'''
    
    data = new_price_data_frame.values
    '''Row[0]	ASIN[1]	SKU[2]	UPC[3]	Store[4]	SaleChan[5]	Status[6]	URL[7]	Price[8]'''#data COLLS
    cell = []
    rows = []
    az_fee = 0.15
    profit = 0.12
    coef = (1+profit)/(1-az_fee)
    
    with open(out_folder+'bqool_inv_file.txt','w',encoding = "ISO-8859-1") as f:
        f.write('FileType = repricing,  Version = 1.2.2 (Please do not edit this line or this will result in error when uploading)\n')
        f.write('\t'.join(['Channel','SellerSKU','Cost','Rule Name','Min Price','Max Price','Shipping','add-delete','Group','Enable Repricing\n']))
        for each in data:

            cell = ['cell[0]','cell[1]','cell[2]','cell[3]','cell[4]','cell[5]','cell[6]','cell[7]','cell[8]','cell[9]']
            cell[0] = 'Amazon US' #Channel
            cell[1] = str(each[2])#SellerSKU
            cell[2] = ''#Cost
            cell[3] = '0-10$'#Rule Name
            
            #cell[4] #Min Price
            if each[8] != 9999999:
                cell[4] = str(round((each[8]*coef),2))
                cell[9] = '1\n'
            else:
                cell[4] = '9999999' #price is each[8] and is int
                cell[9] = '0\n'
            
            if each[6] != 'active':#check status!
                cell[9] = '0\n'
            
            
            cell[5] = '11000000'#Max Price
            cell[6] = '0'#Shipping
            cell[7] = ''#add-delete
            cell[8] = '123'#Group
            #cell[9] #Enable Repricing
            
            #print(cell)
            rows = rows + ['\t'.join(cell)]
        f.writelines(rows)
    


def file_prep(new_price_data_frame,out_folder):
    amazon_inv_file(new_price_data_frame,out_folder)
    bqool_inv_file(new_price_data_frame,out_folder)

import pandas as pd

if __name__ == "__main__":
    
    end_file_name = 'New Prices.csv'
    data_frame = pd.read_csv(end_file_name , encoding = "ISO-8859-1").drop_duplicates(subset='Store', keep='first', inplace=False)
    
    file_prep(data_frame,'')