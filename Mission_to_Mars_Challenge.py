
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

# Visit Space Images URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'

df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df.to_html()

#Mars Hemispheres
hemi_url = 'https://marshemispheres.com/'

browser.visit(hemi_url)

hemisphere_image_urls = []

html = browser.html
hemi_soup = soup(html, 'html.parser')
images = len(hemi_soup.find_all("p"))

for i in range(images):

    #main page with all links
    hemi_tag = browser.find_by_tag('h3')[i]
    hemi_tag.click()


    #Extract HTML into soup
    html = browser.html
    hemi_link_soup = soup(html, 'html.parser')

    #Capture image URL
    hemi_url_rel = hemi_url + hemi_link_soup.find('a', string="Sample")["href"]

    #Capture image title
    hemi_title = browser.find_by_tag('h2').text

    hemisphere_image_urls.append({'img_url': hemi_url_rel, 'title': hemi_title})

    browser.back()


hemisphere_image_urls

browser.quit()