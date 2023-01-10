from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time
import openai

openai.api_key = "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"

username = ''
password = ''

url = 'https://twitter.com/i/flow/login'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


time.sleep(20)
box = driver.find_element(By.NAME, 'text')
box.send_keys(username)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(20)
pbox = driver.find_element(By.NAME, 'password')
pbox.send_keys(password)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()

time.sleep(10)
def botrun():

    prompt = "tell anything on how to improve wealth as a man latest from reddit"
    
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt= prompt,
        temperature=0.4,
        max_tokens=64,
    )

    tweet = response.choices[0].text
    
    driver.find_element(By.XPATH, '//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys(tweet)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()


schedule.every(1).minutes.do(botrun)
while True:
    schedule.run_pending()
    time.sleep(1)
