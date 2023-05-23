from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

username = "elonmusk"
URL = "https://twitter.com/" + username + "?lang=en"

driver.get(URL)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetss"]')))
except WebDriverException:
    print("Tweets did not appear! Proceeding after timeout")

wait = WebDriverWait(driver, 10)
tweets = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))

for tweet in tweets:
    try:
        tweet_text = WebDriverWait(tweet, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="tweetText"]'))).text
        print("Tweet text\t: " + tweet_text)
    except WebDriverException:
        print("Unable to locate tweet text! Proceeding to the next tweet.")

driver.quit()