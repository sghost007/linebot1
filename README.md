# 安裝django套件
- pip install django


# 建立專案
- django-admin startproject app-name

# 開啟目錄 

# 啟動Server
- python manage.py runserver


# 新增功能
- python manage.py startapp main

# git指令
1.安裝git
2.專案目錄底下

# 初始化本地倉庫  
- git init

# 產生忽略檔案
- .gitignore

# 檔案屬性
- U->UnTacked
- A->Added
- M->Modifed

# 加入控管
- git add <filename>
- git add .
	-  加入所有未控管/變動確認

# 確認儲存
- git commit -m "message" 

# 檢視狀態
- git status

# 檢視commit log 
- git log
# 只顯示一行log
- git log --oneline

# 綁定遠端倉庫 
- git remote add origin https://github.com/sghost007/linebot1.git
- git remote -v

# 複製專案
- git clone https://github.com/sghost007/linebot1

# LINE_CHANNEL_SECRET='be2e9c3505498b9d98355ef027ea4b1f'
# LINE_CHANNEL_ACCESS_TOKEN='d5rOIw7e1oxUiO96ziZRTB5lThYBT0+Vpc6+VwsiOcduq0rj1nCSRoKN5aE/o7a2XqyJh/hS5TORnKfft/KEw2MKkxrx3BzeHGTRpU/OgCfSfSwacdwwwwCwBiil/OgmO4v QdB04t89/1O/w1cDnyilFU='#

# 同步資料庫
- python manage.py migrate

# 同步本地跟雲端倉庫
- git push