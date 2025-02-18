from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import json

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
collegedata = []
driver = webdriver.Chrome(options=options)
with open('collegeinfo.txt', 'r') as file:
    json_string = file.read()
    data = json.loads(json_string)
    collegedata = data

data = collegedata[0:10]

driver.implicitly_wait(30)

driver.get("https://en.wikipedia.org/wiki/University_of_Houston–Clear_Lake")
time.sleep(1.5)

for i in range(len(data)):
    if data[i][1] != "":
        searchbar = driver.find_elements(By.CLASS_NAME, "cdx-text-input__input")[0]
        searchbar.send_keys(data[i][2])
        time.sleep(2)
        listitem = driver.find_elements(By.CLASS_NAME, "cdx-menu__listbox")[0]
        it = listitem.find_elements(By.TAG_NAME, "li")[0]
        a = it.find_element(By.TAG_NAME, "a")
        a.click()
        time.sleep(2)
        table = driver.find_elements(By.CSS_SELECTOR, ".infobox.vcard")[0]
        grids = table.find_elements(By.CLASS_NAME, "infobox-image")[0]
        img = grids.find_element(By.TAG_NAME, "img")
        imgurl = img.get_attribute('src')
        spl = imgurl.split('.')[-1]
        img_data = requests.get(imgurl).content
        with open(f'./images/{data[i][1]}.{spl}', 'wb') as handler:
            handler.write(img_data)
        time.sleep(2)

# print(collegedata)

driver.quit()
