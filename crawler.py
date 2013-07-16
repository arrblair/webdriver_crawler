from selenium import webdriver

# populate with the URLs of sites that you need to crawl
sites_to_crawl = []
# I usually use Chrome, but most popular browsers are available
driver = webdriver.Chrome()

for site in sites_to_crawl:
    driver.get(site)
    # - do things a user would while on site
    # - record results
