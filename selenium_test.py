from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    driver = webdriver.Firefox()
    base_url = "http://162.246.157.121:8000/"
    driver.get(base_url)
    elem_name = driver.find_element_by_id("name")
    assert elem_name != None
    elem_about = driver.find_element_by_id("about")
    assert elem_about != None
    elem_education = driver.find_element_by_id("education")
    assert elem_education != None
    elem_skills = driver.find_element_by_id("skills")
    assert elem_skills != None
    elem_work = driver.find_element_by_id("work")
    assert elem_work != None
    elem_contact = driver.find_element_by_id("contact")
    assert elem_contact != None
    print("pass")

test_home()
