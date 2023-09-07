#!/usr/bin/env python
# coding: utf-8

# In[22]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[96]:


# connect to website

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ'
# URL = 'https://www.amazon.com/Got-Data-MIS-Business-Analyst/dp/B08LL786NK/ref=d_gear_dw_dp_gn_sccl_2_5/134-6269374-2130855?pd_rd_w=5uOfN&content-id=amzn1.sym.98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_p=98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_r=P5H7JRPBDMVWRG799JVT&pd_rd_wg=tMjyp&pd_rd_r=cbd623c2-b2c4-4822-acb4-9745baff7d81&pd_rd_i=B08LL786NK&psc=1'

headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT": "1", "Connection" : "Close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id = 'productTitle').get_text()

price = soup2.find(id = 'corePriceDisplay_desktop_feature_div').get_text()


print (title)
print (price)




# In[ ]:





# In[105]:


title = title.strip()
price = price.strip()  [1:6]

print(title)
print(price)


# In[ ]:


import datetime

today = datetime.date(2021, 8, 21)
print(today)


# In[114]:


import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

# type(data)

with open('AmazonWebScraperDataset.csv', 'w', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[129]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Elijah\AmazonWebScraperDataset.csv')

print(df)


# In[115]:


# Date or Time Stamp
# import datetime

# today = datetime.date(2021, 8, 21)
# print(today)


# In[170]:


# Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[171]:



def check_price():
    # connect to website

    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ'
# URL = 'https://www.amazon.com/Got-Data-MIS-Business-Analyst/dp/B08LL786NK/ref=d_gear_dw_dp_gn_sccl_2_5/134-6269374-2130855?pd_rd_w=5uOfN&content-id=amzn1.sym.98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_p=98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_r=P5H7JRPBDMVWRG799JVT&pd_rd_wg=tMjyp&pd_rd_r=cbd623c2-b2c4-4822-acb4-9745baff7d81&pd_rd_i=B08LL786NK&psc=1'

    headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT": "1", "Connection" : "Close", "Upgrade-Insecure-Requests": "1"}

    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id = 'productTitle').get_text()

    price = soup2.find(id = 'corePriceDisplay_desktop_feature_div').get_text()


    title = title.strip()
    price = price.strip()  [1:6]
    
    import datetime
    today = datetime.date.today()
    
    import csv
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline = '', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    


# In[ ]:


# Putting a timer to update the data (csv file) in intervals
while(True):
    check_price()
    time.sleep(2)


# In[172]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Elijah\AmazonWebScraperDataset.csv')

print(df)


# In[ ]:





# In[ ]:




