from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def test_scores_service():
    driver = webdriver.Chrome(executable_path="C:\Ohad\Devops\ChromeWebdriver\chromedriver.exe")
    driver.get("http://127.0.0.1:5000")
    try:
        score = int(driver.find_element_by_id("score").text)
    except:
        score = -1
    driver.close()
    return ((1 <= score) and (score <= 1000))

def main_function():
    if (test_scores_service()):
        exit(0)
    else:
        exit(-1)


main_function()

