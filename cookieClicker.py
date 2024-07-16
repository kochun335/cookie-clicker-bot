import time

from selenium import webdriver
from selenium.webdriver.common.by import By

START_CHECK_FREQUENCY = 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

# Get all the upgrades
upgrades_div = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrades = []

for update_div in upgrades_div:
    upgrades.append(update_div.get_attribute("id"))

# Define a timer to check for upgrades for every 5 seconds
start_time = time.time()
cur_time = start_time
check_frequency = START_CHECK_FREQUENCY

while True:
    if time.time() - start_time > 24000:
        break
    elif (time.time() - start_time) % 120 == 0:
        if check_frequency < 300:
            check_frequency = check_frequency * 1.3
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()

    if time.time() - cur_time > check_frequency:
        # Replace current time
        cur_time = time.time()

        # Get the first unavailable upgrade
        first_unavail_upgrade_div = driver.find_element(By.CLASS_NAME, "grayed").get_attribute("id")
        unavail_upgrade_index = upgrades.index(first_unavail_upgrade_div)

        # Use the first unavailable upgrade index to look for the most expensive upgrade
        if unavail_upgrade_index != 0:
            most_exp_upgrade_id = upgrades[unavail_upgrade_index - 1]
            most_exp_upgrade_div = driver.find_element(By.ID, most_exp_upgrade_id)
            if most_exp_upgrade_div is not None:
                print(most_exp_upgrade_div.get_attribute("id "))
                most_exp_upgrade_div.click()

print(driver.find_element(By.ID, "cps").text)
driver.quit()
