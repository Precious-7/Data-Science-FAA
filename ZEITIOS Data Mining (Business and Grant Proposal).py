#!/usr/bin/env python
# coding: utf-8

# In[113]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[132]:


# connect to website

URL = 'https://new.nsf.gov/funding/opportunities/us-uk-research-collaboration-under-nsf'
# URL = 'https://www.amazon.com/Got-Data-MIS-Business-Analyst/dp/B08LL786NK/ref=d_gear_dw_dp_gn_sccl_2_5/134-6269374-2130855?pd_rd_w=5uOfN&content-id=amzn1.sym.98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_p=98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_r=P5H7JRPBDMVWRG799JVT&pd_rd_wg=tMjyp&pd_rd_r=cbd623c2-b2c4-4822-acb4-9745baff7d81&pd_rd_i=B08LL786NK&psc=1'

headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT": "1", "Connection" : "Close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

c1 = soup2.find('span', {'class' : 'visually-hidden focusable skip-link'}).get_text()


# c2 = soup2.find('div', {'class' : 'dcl__content'}).get_text()

# c3 = soup2.find('div', {'class' : "view-content-header__deadline"}).get_text()

# price = soup2.find(id = 'corePriceDisplay_desktop_feature_div').get_text()'class' : "view-content-header__deadline"

print(c1)
# print (c11)
#print (c2)
#print (c3)

# import csv
# header = ['Title', 'Price', 'Date']
# data = [title, price, today]
# print (price)


# In[130]:


c1 = c1.strip() [1:15]
print(c1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




