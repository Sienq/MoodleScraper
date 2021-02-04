from selenium import webdriver
# from bs4 import BeautifulSoup not yet

CRIDENTIALS_FILE = "cridentials.txt"

class moodleConstants:

    LOGIN_PAGE_URL = "https://logowanie.pg.edu.pl/login?service=https%3A%2F%2Fenauczanie.pg.edu.pl%2Fmoodle%2Flogin%2Findex.php%3FauthCAS%3DCAS"
    NICK_FIELD_ID = 'username'
    PASSWORD_FIELD_ID = 'password'
    LOGIN_BUTTON_ID = 'submit_button'
    
    PROCEED_BUTTON_NAME = 'submit'

def getCridentials():

    with open(CRIDENTIALS_FILE, "r") as f:
        
        cridentials = f.readlines()
        nick = cridentials[0].strip()
        password = cridentials[1].strip()

        return nick, password

driver = webdriver.Chrome()

def logIntoMoodle():

    nick, password = getCridentials()
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


logIntoMoodle()