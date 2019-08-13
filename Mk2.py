import selenium webdriver as webdriver
from googlesearch import search



def get_results(search_term):
  url = "https://www.startpage.com"
  browser = webdriver.Firefox()
  browser.get(url)
  search_box = browser.find_element_by_id("query")
  search_box.send_keys(search_term)
  search_box.submit()
  try:
    links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
  except:
    links = browser.find_elements_by_xpath("//h3//a")
  results = []
  for link in links:
    href = link.get_attribute("href")
    print (href)
    results.append(href)
  browser.close()
  return results
get_results("dog")

feedUrls = results
email(feedUrls)
  
def email(feedUrls):
searchVar1 = feedUrls
for searchVar2 in search(searchVar1, stop=20):
    print(url)
