
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def scrape_info():
    # =========================NASA Mars News=================================
    browser = Browser("chrome",  headless=False)

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")


    news_title = soup.find_all("div", class_="content_title")[0].text
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    browser.quit()
    # =========================================================================


    # =========================JPL Mars Space Images - Featured Image==========

    browser = Browser("chrome",  headless=False)

    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    jpl_url = "https://www.jpl.nasa.gov"

    href = soup.find_all("section", class_="primary_media_feature")[0].footer.a['data-fancybox-href']

    featured_image_url = jpl_url + href
    browser.quit()
    # =========================================================================


    # =========================Mars Facts======================================
    browser = Browser("chrome",  headless=False)

    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")
    mars_weather = soup.find_all("ol", id="stream-items-id")[0].li.p.text
    browser.quit()
    # =========================================================================



    # =========================Mars Hemispheres================================
    url = "https://space-facts.com/mars/"

    tables = pd.read_html(url)
    mars_facts_df = tables[0]
    mars_facts_df.set_index(0, inplace=True)
    mars_html = mars_facts_df.to_html()
    cleaned_html = mars_html.replace('\n', '')
    mars_facts_df.to_html("Mars_facts_html_table.html")


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]

    # =========================================================================

    scrape_mars = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather":mars_weather,
        "mars_fact_table":cleaned_html,
        "hemisphere_image_urls":hemisphere_image_urls

    }
    print("Done Scraping")
    return scrape_mars

