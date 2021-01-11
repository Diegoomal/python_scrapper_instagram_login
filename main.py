import sys
from credentials import userName, password
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def ExecuteLogin():
    try:  
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        driver.get('https://www.instagram.com/accounts/login/')

        # util login page appear
        wait = WebDriverWait(driver, 300)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "KPnG0")))

        userElemnt = driver.find_element_by_name('username')
        userElemnt.clear()
        userElemnt.send_keys(userName)
        userElemnt.send_keys(Keys.RETURN)

        passwElemnt = driver.find_element_by_name('password')
        passwElemnt.clear()
        passwElemnt.send_keys(password)
        passwElemnt.send_keys(Keys.RETURN)

        submitElement = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]")))
        submitElement.click()
        
    except NoSuchElementException as err:
        print("NoSuchElementException: {0}".format(err))
        driver.quit()
        driver.close()
    except ElementClickInterceptedException as err:
        print("ElementClickInterceptedException: {0}".format(err))
        driver.quit()
        driver.close()
    except TimeoutException as err:
        print("TimeoutException: {0}".format(err))
        driver.quit()
        driver.close()
    except StaleElementReferenceException as err:
        print("StaleElementReferenceException: {0}".format(err))
        driver.quit()
        driver.close()
    except:
        print("Exception - Unexpected error:", sys.exc_info()[0])
        driver.quit()
        driver.close()
    finally:
        pass

if __name__ == "__main__":

    ExecuteLogin()

    input("Press Enter to finish...")