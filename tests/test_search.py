"""
These tests cover DuckDuckGo searches.
"""

import pytest
import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('PHRASE', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, PHRASE):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  #PHRASE = "panda"
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for "panda"
  search_page.search(PHRASE)

  # Then the search result title contains "panda"
  #from selenium.webdriver.support.ui import WebDriverWait 
  #from selenium.webdriver.support import expected_conditions as EC 
  #WebDriverWait (driver, 10).until(EC.title_contains(PHRASE)) 
  #import time
  #time.sleep(5)
 
  
  # And the search result query is "panda"
  assert PHRASE == result_page.search_input_value()
  
  # And the search result links pertain to "panda"
  titles = result_page.result_link_titles()
  matches = [t for t in titles if PHRASE.lower() in t.lower()]
  assert len(matches) > 0

  # Then the search result title contains "panda"
  assert PHRASE in result_page.title()

#def new_func(PHRASE):
    #return PHRASE