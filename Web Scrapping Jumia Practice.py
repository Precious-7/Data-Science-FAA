#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[91]:


# connect to website

URL = 'https://www.jumia.com.ng/fashion-men-shorts-summer-gyms-workout-sportswear-133997701.html'
# URL = 'https://www.amazon.com/Got-Data-MIS-Business-Analyst/dp/B08LL786NK/ref=d_gear_dw_dp_gn_sccl_2_5/134-6269374-2130855?pd_rd_w=5uOfN&content-id=amzn1.sym.98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_p=98cd7395-1427-4463-ba2f-d9a4c6e9990c&pf_rd_r=P5H7JRPBDMVWRG799JVT&pd_rd_wg=tMjyp&pd_rd_r=cbd623c2-b2c4-4822-acb4-9745baff7d81&pd_rd_i=B08LL786NK&psc=1'

headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT": "1", "Connection" : "Close", "Upgrade-Insecure-Requests": "1"}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")
# print(soup1)

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
# print(soup2)

title = soup2.find('div', {"class" : "-fs0 -pls -prl"}).get_text()
# print(title)

# price = soup2.find('div', {"class" : "-b -ltr -tal -fs24"}).get_text()
# price_text = div.text

print (title)
print (price)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




