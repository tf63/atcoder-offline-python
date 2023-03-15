from selenium import webdriver

FILENAME = "a.png"

# set driver and url
driver = webdriver.Chrome("./chromedriver")
url = "https://www.rakuten.co.jp/"
driver.get(url)

# get width and height of the page
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")

# set window size
driver.set_window_size(w, h)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()
