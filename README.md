# 自動網路認證腳本

這是一個使用 Selenium 自動進行網路認證的 Python 腳本。

## 功能

- 定期檢查網路連接狀態
- 自動登入網路認證頁面
- 支援無頭瀏覽器模式
- 可配置的執行間隔和顯示選項

## 安裝

1. 確保已安裝 Python 3.6 或更高版本。
2. 安裝所需的依賴:

   ```
   pip install selenium webdriver_manager
   ```

3. 下載與您的 Chrome 瀏覽器版本相匹配的 ChromeDriver，並將其放置在專案的 `chromedriver-win64` 資料夾中。配置

   ```
   https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
   ```

在專案根目錄建立一個 `settings.json` 檔案，包含以下內容:

```json
{
  "empNo": "您的員工編號",
  "password": "您的密碼",
  "interval": 5,
  "showBrowser": "N"
}
```

- `empNo`: 您的員工編號
- `password`: 您的密碼
- `interval`: 檢查間隔(秒)
- `showBrowser`: 是否顯示瀏覽器 ("Y" 顯示, "N" 不顯示)

## 使用

執行以下指令啟動腳本:

```
python main.py
```

腳本將按照設定的間隔時間自動檢查網路連接並在需要時進行認證。

## 注意事項

- 請確保 `settings.json` 檔案中的資訊正確且安全。
- 腳本使用 ChromeDriver，請確保已正確安裝並配置。
- 如遇到問題，請檢查控制台輸出的錯誤訊息。

## 授權

[在此添加您的授權資訊]
