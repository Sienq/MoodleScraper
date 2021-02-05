
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(chrome_options=chrome_options)

class moodleConstants:

    LOGIN_PAGE_URL = "https://logowanie.pg.edu.pl/login?service=https%3A%2F%2Fenauczanie.pg.edu.pl%2Fmoodle%2Flogin%2Findex.php%3FauthCAS%3DCAS"
    NICK_FIELD_ID = 'username'
    PASSWORD_FIELD_ID = 'password'
    LOGIN_BUTTON_ID = 'submit_button'
    
    PROCEED_BUTTON_NAME = 'submit'

    CALENDAR_LINK_CLASS = 'gotocal'
    CALENDAR_LINK_URL = 'https://enauczanie.pg.edu.pl/moodle/calendar/view.php?view=upcoming'



def getEventsPageSource(credentials):

    nick, password = credentials[0], credentials[1]
    driver.get(moodleConstants.LOGIN_PAGE_URL)

    username_field = driver.find_element_by_id(moodleConstants.NICK_FIELD_ID)
    username_field.clear()
    username_field.send_keys(nick)

    password_field = driver.find_element_by_name(moodleConstants.PASSWORD_FIELD_ID)
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id(moodleConstants.LOGIN_BUTTON_ID)
    login_button.click()

    try:
        proceed_button = driver.find_element_by_name(moodleConstants.PROCEED_BUTTON_NAME)
        proceed_button.click()

    except NoSuchElementException:
        pass
    
    try:
        cookie_close = driver.find_element_by_class_name("close-cookie-panel")
        cookie_close.click()
    
    except NoSuchElementException:
        pass

    calendar_link = driver.find_element_by_xpath('//a[@href="'+moodleConstants.CALENDAR_LINK_URL+'"]')
    calendar_link.click()

    return driver.page_source
