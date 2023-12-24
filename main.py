from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium():
    driver = webdriver.Chrome()

    driver.get("https://www.yad2.co.il/realestate/rent?topArea=41&area=12&city=8400")

    title = driver.title
    assert title == '\u202bנדל״ן להשכרה ברחובות | נדל"ן להשכרה יד2\u202c'

    # driver.implicitly_wait(0.5)
    #
    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    #
    # text_box.send_keys("Selenium")
    # submit_button.click()
    #
    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"

    driver.quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_selenium()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
