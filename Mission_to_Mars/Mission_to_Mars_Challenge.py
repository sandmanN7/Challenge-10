#!/usr/bin/env python
# coding: utf-8

# In[36]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[37]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[38]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[39]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[40]:


slide_elem.find('div', class_='content_title')


# In[41]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[42]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Image
# 

# In[43]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[44]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[45]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[46]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[47]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[48]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[49]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[50]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[51]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
img_soup = soup(html, 'html.parser')

for x in range(4):
    browser.find_by_css('div[class="description"] a')[x].click()
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    title = img_soup.find('h2', class_='title').get_text()
    
    link = img_soup.find(lambda tag:tag.name=="a" and "Sample" in tag.text)
    img_url = link.get('href')
    
    hemisphere = {}
    hemisphere['img_url'] = img_url
    hemisphere['title'] = title
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()


# In[52]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[53]:


# 5. Quit the browser
browser.quit()


# In[ ]:




