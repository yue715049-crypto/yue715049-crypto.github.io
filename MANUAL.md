# 悅來越好玩 - 網站設定手冊 (Configuration Manual)

這份手冊將引導您如何設定與管理您的 Pelican 旅遊部落格。所有的設定都在 `pelicanconf.py` 檔案中進行。

## 1. 基本資訊設定 (Basic Info)
在 `pelicanconf.py` 的最上方，您可以修改網站的基本資訊：

```python
AUTHOR = 'Tingyue Lai'       # 您的名字
SITENAME = '悅來越好玩'       # 網站名稱
SITEURL = ''                 # 網站網址 (本地開發時留空)
```

## 2. 選單設定 (Menu)
您可以自由新增或修改頂部的導航選單。支援下拉式選單 (Dropdown)。

找到 `MENUITEMS` 設定區塊： 

```python
MENUITEMS = (
    ('首頁', '/'),  # 一般連結：('顯示名稱', '連結網址')
    
    # 下拉式選單：('顯示名稱', '#', (子選單項目...))
    ('海外旅遊', '#', (
        ('日本', '/category/japan.html'),
        ('韓國', '/category/korea.html'),
        ('泰國', '/category/thailand.html'),
    )),
    
    ('關於我', '/pages/about.html'),
)
```

## 3. Google 服務整合 (Google Integrations)
為了讓您的網站能賺取廣告收益並被搜尋引擎找到，請填入您的專屬 ID。

找到 `Google Analytics & Ads & Search Console` 區塊：

### Google AdSense (廣告)
```python
GOOGLE_ADSENSE = {
    'client': 'ca-pub-XXXXXXXXXXXXXXXX', # 替換成您的 Client ID
    'slot': 'XXXXXXXXXX'                 # 替換成您的 Slot ID
}
```

### Google Search Console (搜尋引擎驗證)
```python
GOOGLE_SEARCH_CONSOLE = 'VerificationCodeHere' # 替換成 Google 提供的驗證碼
```
*注意：如果您還沒有驗證碼，請到 Google Search Console 申請，並選擇 "HTML Tag" 驗證方式，複製 `content="..."` 裡面的代碼即可。*

## 4. 網站圖示 (Favicon)
預設的網站圖示位於 `content/images/favicon.ico`。
如果您想更換圖示：
1. 準備一個 `.ico` 或 `.png` 圖片。
2. 將圖片命名為 `favicon.ico`。
3. 覆蓋 `content/images/` 資料夾中的同名檔案。

## 5. SEO 設定
網站已經自動設定好 SEO 功能，會根據您的文章內容自動產生：
- **Description (描述)**: 來自文章摘要。
- **Keywords (關鍵字)**: 來自文章標籤 (Tags)。
- **Open Graph**: 讓分享到 Facebook/Line 時有漂亮的預覽圖。

您只需要專注於撰寫高品質的文章，並記得為每篇文章加上 `Tags` 即可。

## 6. 部署到 GitHub (Deployment)
我已經為您準備好了自動部署的檔案。請依照以下步驟將網站推送到 GitHub：

1.  **建立 GitHub Repository**:
    - 到 GitHub 新增一個 Repository (例如 `travel-blog`)。
    - **不要** 勾選 "Initialize with README"。

2.  **設定網址 (publishconf.py)**:
    - 打開 `publishconf.py`。
    - 修改 `SITEURL` 為您的 GitHub Pages 網址 (例如 `https://yourname.github.io/travel-blog`)。

3.  **推送到 GitHub**:
    在終端機執行以下指令 (請將 `<URL>` 換成您的 Repository 網址)：
    ```bash
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin <URL>
    git push -u origin main
    ```

4.  **開啟 GitHub Pages**:
    - 到 GitHub Repository 的 **Settings** > **Pages**。
    - 在 **Source** 選擇 `gh-pages` branch (這個 branch 會在第一次部署成功後自動出現)。
    - 點擊 **Save**。

之後，每次您更新文章並執行 `git push`，網站就會自動更新！

---
**本地預覽 (Local Preview)**
在終端機輸入：
```bash
pelican content && pelican --listen
```
