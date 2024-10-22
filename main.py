# 要安裝的pip install selenium webdriver_manager

from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
# 讀取外部檔案settings.json
with open('settings.json') as f:
    settings = json.load(f)
username = settings['empNo']
password = settings['password']
interval = settings['interval']
showBrowser = settings['showBrowser']
# Convert showBrowser value to boolean
headless = False if showBrowser == 'Y' else True



def main():
    
    # 設定員工編號和密碼
    # username = ""
    # password = ""
    
    # 設定執行間隔(秒)
    # interval = 5


    # 設定是否使用 headless 模式   (是否隱藏瀏覽器)    
    # headless = False  # 設為 True 以隱藏瀏覽器，設為 False 以顯示瀏覽器


    # 初始化 WebDriver
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    # 獲取當前腳本所在目錄
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 設置 ChromeDriver 路徑
    chromedriver_path = os.path.join(current_dir, "chromedriver-win64", "chromedriver.exe")
    print(f"ChromeDriver 路徑: {chromedriver_path}")  # 印出路徑以確保正確

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        while True:
            try:
                # 打開目標網址
                driver.get("https://learn.microsoft.com/")
                # 使用顯式等待等待頁面加載
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{current_time} - 連線成功")
            except:
                try:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{current_time} - 無法連線，嘗試登入")

                    # 打開登入頁面
                    driver.get("https://hltchnet.tzuchi.com.tw:1003/portal?")

                    # 使用顯式等待等待頁面加載
                    WebDriverWait(driver, 10).until(
                        EC.any_of(
                            EC.presence_of_element_located((By.NAME, "username")),
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '上網認證成功')]"))
                        )
                    )

                    # 檢查是否已登入
                    if "上網認證成功" in driver.page_source:
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"{current_time} - 已登入")
                    else:
                        # 填寫員工編號
                        username_field = driver.find_element(By.NAME, "username")
                        username_field.send_keys(username)

                        # 填寫密碼
                        password_field = driver.find_element(By.NAME, "password")
                        password_field.send_keys(password)

                        # 提交表單
                        password_field.send_keys(Keys.RETURN)

                        # 使用顯式等待等待登入成功
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '上網認證成功')]"))
                        )

                        # 再次檢查是否登入成功
                        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        if "上網認證成功" in driver.page_source:
                            print(f"{current_time} - 確認登入成功")
                        else:
                            print(f"{current_time} - 登入失敗")
                except Exception as err:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{current_time} - 登入失敗 {err.__class__.__name__}: {err}")
            # 每隔 5 秒執行一次
            time.sleep(interval)

    finally:
        # 關閉瀏覽器
        driver.quit()

if __name__ == "__main__":
    main()