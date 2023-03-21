import os

from selenium import webdriver
from selenium.webdriver import ChromeOptions


def save_screenshot(url, filename):
    """
    webサイトのスクリーンショットを全画面で撮影し，/work/out/img/filenameに保存する

    Args:
        url: WebサイトのURL
        filename: 保存する画像名 image.png
    Returns: (None)
    """

    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Selenium サーバへ接続
    print("Connecting selenium server...")
    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        options=webdriver.ChromeOptions(),
    )

    # 待機
    driver.implicitly_wait(5)

    # File Name
    os.makedirs("out/img", exist_ok=True)
    FILENAME = f"/work/out/img/{filename}"
    print(f"Save screenshot {FILENAME} ...")

    # set driver and url
    driver.get(url)

    # get width and height of the page
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    print(f"Image size: ({w}, {h})")
    # set window size
    driver.set_window_size(w, h)

    # Get Screen Shot
    driver.save_screenshot(FILENAME)

    # Close Web Browser
    driver.quit()
