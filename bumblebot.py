from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
from selenium.common.exceptions import NoSuchElementException        


FB_EMAIL = "myemail@facebook.com"
FB_PASSWORD = "mypassword"

print("======= Bumble Bot V1 ========")

# chrome_driver_path = YOUR CHROME DRIVER PATH
driver = webdriver.Chrome()

driver.get("https://bumble.com/get-started")

sleep(5)
# login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
login_button.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)


email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

print("======= Login with facebook Success =======")

driver.switch_to.window(base_window)
print(driver.title)

sleep(8)

for n in range(100):
  sleep(7)
  try:
    # print("======= Preparing swipe right  =======")
    name = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[1]/article/div[2]/section/header/h1/span[1]')
    age = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[1]/article/div[2]/section/header/h1/span[2]')
    # location = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[6]/article/div[2]/section/div/section/div[1]/span')
    try:
      #identify element
      about = driver.find_element_by_class_name('encounters-story-profile__occupation')
      name_and_age = f"======= Swiping right {name.text} {age.text} years old. About {name.text} {about.text} ======="
      #NoSuchElementException thrown if not present
    except NoSuchElementException:
      name_and_age = f"======= Swiping right {name.text} {age.text} years old. ======="
        
    print(name_and_age)

    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 5):
      driver.execute_script("window.scrollTo(0, {});".format(i))

    like_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
    like_button.click()
  except ElementClickInterceptedException:
    try:
      sleep(2)
    except NoSuchElementException:
      sleep(2)

driver.quit()