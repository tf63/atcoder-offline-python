from selenium import webdriver
from selenium.webdriver import ChromeOptions


def save_screenshot(url):
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # <=これを追加
    # options.add_argument('--disable-gpu')  # ページによって必要な場合がある模様

    # Selenium サーバへ接続
    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=webdriver.ChromeOptions(),
    )
    driver.implicitly_wait(5)  # seconds

    # driver = webdriver.Chrome(options=options)

    # File Name
    FILENAME = "/work/out/img/screen.png"
    print(FILENAME)
    # set driver and url
    url = "https://trend-tracer.com/"
    driver.get(url)

    # get width and height of the page
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    print(w, h)
    # set window size
    driver.set_window_size(w, h)

    # Get Screen Shot
    driver.save_screenshot(FILENAME)

    # Close Web Browser
    driver.quit()
